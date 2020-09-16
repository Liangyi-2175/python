# -*- coding: utf-8 -*-
import json

from hagworm.extend.asyncio.net import HTTPJsonClient
from hagworm.extend.asyncio.task import IntervalTask
from requests import ReadTimeout

from hagworm.extend.base import Utils
from m_apoll import Apoll


class ApolloClient:
    def __init__(self, app_id=None, cluster=None, config_server_url=None, timeout=30,
                 ip=None, notification_map=None):

        self.appId = app_id
        self.cluster = cluster
        self.timeout = timeout
        self.stopped = False
        self.init_ip(ip)

        self._cache = {}

        self.config_server_url = config_server_url

        self._notification_map = notification_map if notification_map else {}

    def init_ip(self, ip):
        if ip:
            self.ip = ip
        else:
            import socket
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(('8.8.8.8', 53))
                ip = s.getsockname()[0]
            finally:
                s.close()

            self.ip = ip

    async def start(self):

        if len(self._cache) == 0:
            await self._long_poll()

        IntervalTask.create(1, False, self._long_poll)

    def _listener(self):
        self._long_poll()

    async def _uncached_http_get(self, http_client, namespace='application'):

        url = '{}/configs/{}/{}/{}?ip={}'.format(self.config_server_url, self.appId, self.cluster, namespace, self.ip)

        data = await http_client.get(url=url)
        Utils.log.debug(url)

        if data:
            self._cache[namespace] = data['configurations']

            Utils.log.info(f"Updated local cache for namespace {namespace} release key {data['releaseKey']}: \n"
                           f"{repr(self._cache[namespace])}")

    async def _long_poll(self):
        url = '{}/notifications/v2'.format(self.config_server_url)
        notifications = []
        for key in self._notification_map:
            notification_id = self._notification_map[key]
            notifications.append({
                'namespaceName': key,
                'notificationId': notification_id
            })
        try:

            params = {
                'appId': self.appId,
                'cluster': self.cluster,
                'notifications': json.dumps(notifications, ensure_ascii=False)
            }

            Utils.log.debug("url:%s  --  params:%s" % (url, params))
            http_client = HTTPJsonClient()
            data = await http_client.get(url=url, params=params)

            if data:

                for entry in data:
                    ns = entry['namespaceName']
                    nid = entry['notificationId']

                    Utils.log.info(f"{ns} has changes: notificationId={nid}")

                    await self._uncached_http_get(http_client, ns)
                    self._notification_map[ns] = nid

                # 加载配置
                self.initialize(self._cache)

            else:
                if len(self._cache) == 0:
                    raise ValueError

        except ReadTimeout as e:
            Utils.log.debug('No change, read time out...')

    def initialize(self, data):
        apoll = Apoll()
        apoll.set(data)
