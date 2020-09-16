# Launcher config
import asyncio
import os

import aiohttp
from hagworm.extend.asyncio.base import MultiTasks, AsyncCirculator
from hagworm.extend.asyncio.net import HTTPClient
from hagworm.extend.base import Utils
from hagworm.frame.stress_tests import Launcher, Runner, TaskInterface


TASK_NUm = 1
PROCESS_NUM = 1
MULTI_TASK_COUNT = 200

# Task run config
TASK_WAIT_TIME = 2

# Client request config
SERVICE_HOTS = 'http://dev.jiayouxueba.com'
SERVICE_API = '/down'
RETRY_COUNT = 1
REQ_TIME_OUT = aiohttp.client.ClientTimeout(total=120, connect=20, sock_read=120, sock_connect=20)
APP_NAME_LIST = []

# Report event name
REQUEST = "Request"
CLIENT = "Client"

# log config
LOG_FILE_PATH = "./log"
os.path.exists(LOG_FILE_PATH) or os.makedirs(LOG_FILE_PATH)
LOG_LEVEL = "INFO"



class Task(TaskInterface):

    async def parse(self):
        global RETRY_COUNT, SERVICE_HOTS, REQUEST, CLIENT, PARAMS, SERVICE_API

        request_start_time = self.loop_time()

        try:
            url = SERVICE_HOTS + SERVICE_API
            headers = {"X-Payload": str(request_start_time), "Content-Type": "application/x-www-form-urlencoded"}
            resp = await HTTPClient(retry_count=RETRY_COUNT, timeout=REQ_TIME_OUT).get(url, headers=headers)
            Utils.log.info(f'resp:{resp}')
        except aiohttp.ClientResponseError as err:
            self.log.error(f"The response of server is fail, Exception is {err}")
            self.failure(REQUEST, self.loop_time() - float(request_start_time))

        except aiohttp.ClientError as err:
            self.log.error(f"The request  of client is fail, Exception is {err}")
            self.failure(CLIENT, self.loop_time() - float(request_start_time))

        except Exception as err:
            self.log.error(f"The unknown error of client, Exception is {err}")
            self.failure(CLIENT, self.loop_time() - float(request_start_time))


        else:

            if resp != None:
                self.log.info(f"The response is success, resp is {resp}")
                    #request_time = resp.headers.get('X-Payload', None)
                    #Utils.log.info(f"request_time{request_time}")
                    #if request_time:
                self.success(REQUEST, self.loop_time() - float(request_start_time))

            else:
                self.log.info(f"The response is Neno")
                self.failure(REQUEST, self.loop_time() - float(request_start_time))




    async def run(self):

        global MULTI_TASK_COUNT, TASK_WAIT_TIME

        tasks = MultiTasks()

        async for _ in AsyncCirculator(max_times=MULTI_TASK_COUNT):
            tasks.append(self.parse())

        await tasks

        await asyncio.sleep(TASK_WAIT_TIME)


if __name__ == r'__main__':
    Launcher(log_file_path=LOG_FILE_PATH,
             log_level=LOG_LEVEL,
             process_number=PROCESS_NUM).\
        run(Runner(Task).run, 1, TASK_NUm)