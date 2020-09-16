from xiaoliang.pyapollo import ApolloClient
from xiaoliang.log import Logger
config_server_url = 'http://47.110.5.120:18020'
app_id = 'jyxb-activity'
cluster = 'dev'
env = 'DEV'
a = ApolloClient(app_id, cluster, config_server_url)
v = a.get_value(key="config.advert.screen.size")
print(v)



# -*- coding: utf-8 -*-
import json
import logging
import threading
import time
import requests
import logging.config
import os
import socket

CON_LOG = os.path.abspath(
    (os.path.dirname(
        (os.path.dirname(__file__)))) +
    '/config/log.conf')
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


class ApolloClient(object):
    """
    读取Apollo配置
    """

    def __init__(self, app_id, cluster, config_server_url, interval=60, ip=None):

        self.config_server_url = config_server_url
        self.appId = app_id
        self.cluster = cluster
        self.timeout = 60
        self.interval = interval
        self.init_ip(ip)
        self._stopping = False
        self._cache = {}
        self._notification_map = {'application': -1}

    def init_ip(self, ip):
        """
        获取本地IP
        :param ip:
        :return:
        """
        if ip:
            self.ip = ip
        else:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(('8.8.8.8', 53))
                ip = s.getsockname()[0]
            finally:
                s.close()
            self.ip = ip

    def get_value(self, key, default_val=None, namespace='application', auto_fetch_on_cache_miss=False):
        """
        如果没有缓存的时候调用通过不带缓存的Http接口从Apollo读取配置
        如果有缓存的时候通过带缓存的Http接口从Apollo读取配置
        :param key:
        :param default_val:
        :param namespace:
        :param auto_fetch_on_cache_miss:
        :return:
        """
        if namespace not in self._notification_map:
            self._notification_map[namespace] = -1
            # logging.getLogger(__name__).info("Add namespace '%s' to local notification map", namespace)
            logging.info("Add namespace {} to local notification map".format(namespace))

        if namespace not in self._cache:
            self._cache[namespace] = {}
            # logging.getLogger(__name__).info("Add namespace '%s' to local cache", namespace)
            # logging.info("Add namespace '%s' to local cache", namespace)
            logging.info("Add namespace {} to local cache".format(namespace))
            self._long_poll()
        if key in self._cache[namespace]:
            return self._cache[namespace][key]
        else:
            if auto_fetch_on_cache_miss:
                return self._cached_http_get(key, default_val, namespace)
            else:
                return default_val

    def _cached_http_get(self, key, default_val, namespace='application'):
        """
        请求Apollo有缓存
        :param key:
        :param default_val:
        :param namespace:
        :return:
        """
        url = '{}/configfiles/json/{}/{}/{}?ip={}'.format(self.config_server_url, self.appId, self.cluster, namespace,
                                                          self.ip)
        r = requests.get(url)
        if r.ok:
            data = r.json()
            logging.info("_cached_http_get打印data数据：{}".format(data))
            self._cache[namespace] = data
            logging.info('Updated local cache for namespace -->{}'.format(namespace))
        else:
            data = self._cache[namespace]

        if key in data:
            return data[key]
        else:
            return default_val

    def _uncached_http_get(self, namespace='application'):
        """
        请求Apollo无缓存模式
        :param namespace:
        :return:
        """
        url = '{}/configs/{}/{}/{}?ip={}'.format(self.config_server_url, self.appId, self.cluster, namespace, self.ip)

        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            logging.info("_uncached_http_get打印data数据：{}".format(data))
            self._cache[namespace] = data['configurations']
            logging.info("_uncached_http_get打印data数据：{}".format(self._cache))
            logging.info('Updated local cache for namespace {} release key {}: {}'.format(
                namespace, data['releaseKey'],
                repr(self._cache[namespace])))

    def _long_poll(self):
        """
        判断Apollo地址请求是否正常，正常则直接取Apollo配置
        :return:
        """
        url = '{}/notifications/v2'.format(self.config_server_url)
        notifications = []
        for key in self._notification_map:
            notification_id = self._notification_map[key]
            notifications.append({
                'namespaceName': key,
                'notificationId': notification_id
            })

        r = requests.get(url=url, params={
            'appId': self.appId,
            'cluster': self.cluster,
            'notifications': json.dumps(notifications, ensure_ascii=False)
        }, timeout=self.timeout)
        logging.info('Long polling returns {}: url={}'.format(r.status_code, r.request.url))

        if r.status_code == 304:
            # no change, loop
            logging.info('No change, loop...')
            return

        if r.status_code == 200:
            data = r.json()
            for entry in data:
                ns = entry['namespaceName']
                nid = entry['notificationId']
                print("sssss")
                logging.info("{} has changes: notificationId={}".format(ns, nid))
                self._uncached_http_get(ns)
                self._notification_map[ns] = nid
        else:
            logging.error('Sleep...')
            time.sleep(self.timeout)

    def _listener(self):
        logging.info('Entering listener loop...')
        while not self._stopping:
            self._long_poll()
            time.sleep(self.interval)
        logging.info("Listener stopped!")


if __name__ == '__main__':
    config_server_url = "http://47.110.5.120:18020"
    app_id = "jyxb-activity"
    cluster = "dev"
    apollo_client = ApolloClient(app_id, cluster, config_server_url)
    s = apollo_client.get_value(key='config.advert.screen.size')
    print(s)
