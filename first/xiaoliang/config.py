from example.setting import ConfigDynamic
from hagworm.extend.asyncio.base import Launcher

from apoll import ApolloClient
from m_apoll import Apoll
from hagworm.extend.base import Utils



async def main():
    config_server_url = 'http://47.110.5.120:18020'
    app_id = 'ticket-service'
    upload_service_file_type = 'TECH.ticket-service.base'
    cluster = 'develop'

    # app_id = ConfigDynamic.ApolloAppId
    # config_server_url = ConfigDynamic.ApolloConfigServerUrl
    # cluster = ConfigDynamic.ApolloCluster
    notification_map = {
        upload_service_file_type: -1,
    }

    apollo_client = ApolloClient(app_id=app_id, cluster=cluster, config_server_url=config_server_url,
                                 notification_map=notification_map)

    await apollo_client.start()

    apoll_config = Apoll().get()

    place_type_config_str = apoll_config.get(upload_service_file_type, {}).get("place_type", {})
    print(place_type_config_str)
if __name__ == r'__main__':

    Launcher().run(main)
