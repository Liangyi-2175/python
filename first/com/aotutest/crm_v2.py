# -*- coding: utf-8 -*-
from hagworm.extend.asyncio.net import HTTPClient
from hagworm.extend.base import Utils
from hagworm.frame.stress_tests import Launcher, Runner, TaskInterface

host = r'dev6.jiayouxueba.cn'
headers = ''
LOG_FILE_PATH = './log'
LOG_LEVEL = 'INFO'
PROCESS_NUM = '1'
TASK_NUm = 1


class Task(TaskInterface):

    def __init__(self):
        pass

    def run(self):
        self.get_operator_statistics()

    def get_operator_statistics(self):
        resp = HTTPClient.get(host + '/crm-v2/external/operator_statistics/')
        Utils.log.info("运营师基础数据返回结果{}".format(resp))


if __name__ == '__main__':
    Launcher(log_file_path=LOG_FILE_PATH,
             log_level=LOG_LEVEL,
             subprocess=PROCESS_NUM).run(Runner(Task), 1, TASK_NUm)