from hagworm.extend.asyncio.zmq import PublisherWithBuffer
from hagworm.extend.interface import RunnableInterface

from com.stress_test import TaskInterface
from com.stress_test.MultiTasks import MultiTasks
from com.stress_test.Utils import Utils


class Runner(Utils, RunnableInterface):
    """
    脚本任务类的运行类
    """

    def __init__(self, task_cls: TaskInterface):

        global SIGNAL_PROTOCOL, SIGNAL_PORT
        # 初始化实例对象时，将我们的脚本任务类 task_cls 赋给_task_cls实例属性
        self._task_cls = task_cls
        # 将zmq发布类对象赋给_publisher实例对象
        self._publisher = PublisherWithBuffer(f'{SIGNAL_PROTOCOL}://localhost:{SIGNAL_PORT}', False)

    async def run(self, times, task_num):

        self._publisher.open()

        # 将我们的脚本任务打包为多个任务一起执行
        for _ in range(times):

            tasks = MultiTasks()

            for _ in range(task_num):
                # 将zmq发布对象传给我们的任务基类TaskInterface
                # 同时将我们的脚本Task的run方法,塞入到多任务MultiTasks()对象中
                tasks.append(self._task_cls(self._publisher).run())

            await tasks

        await self._publisher.safe_close()