# -*- coding: utf-8 -*-


# log config
import os

from com.stress_test.Launcher import Launcher
from com.stress_test.Runner import Runner
from com.stress_test.TaskInterface import TaskInterface

LOG_FILE_PATH = "./logs"  # 脚本日志路径
os.path.exists(LOG_FILE_PATH) or os.makedirs(LOG_FILE_PATH)  # 生成脚本日志文件目录
LOG_LEVEL = "INFO"  # 脚本日志等级

# Launcher config
PROCESS_NUMBER = 1  # 进程数
TASK_NUM = 1  # 任务数


# 该脚本最终执行的任务数（执行多少次Task） = PROCESS_NUMBER * TASK_NUM * 1


class Task(TaskInterface):
    """
    所有的脚本任务都必须继承TaskInterface类
    """

    async def run(self):
        """
        继承了TaskInterface类后必须重写run方法
        而run方法就是我们用来控制压测主逻辑的
        """

        for index in range(2):

            await self.sleep(0.1)

            resp_time = self.randint(12345, 98765) / 10000

            # 记录脚本运行情况时调用success方法，或者failure方法，
            # 发送一次zmq消息到消息池中，等消息量达到水位,由zmq统一发送
            # success方法或failure方法的第一个参数为自定义的报告事件名称,第二个参数为消耗时间
            if self.randhit([True, False], [32, 8]):
                # 记录成功事件
                self.success(f'Test{index}', resp_time)
            else:
                # 记录失败事件
                self.failure(f'Test{index}', resp_time)


if __name__ == r'__main__':
    # 参数由常量设置
    Launcher(
        log_file_path=LOG_FILE_PATH,
        log_level=LOG_LEVEL,
        process_number=PROCESS_NUMBER
    ).run(Runner(Task).run, 1, TASK_NUM)