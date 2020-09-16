from hagworm.extend.asyncio.zmq import PublisherWithBuffer
from hagworm.extend.interface import RunnableInterface

from com.stress_test.Utils import Utils


class TaskInterface(Utils, RunnableInterface):
    """
    脚本任务类的基类
    实例化对象时初始化一个zmq发布对象，由success方法发送任务成功的消息，failure方法发送任务失败的消息
    """

    def __init__(self, publisher: PublisherWithBuffer):

        self._publisher = publisher

    def success(self, name: str, resp_time: int):

        self._publisher.append(
            (name, r'success', resp_time,)
        )

    def failure(self, name: str, resp_time: int):

        self._publisher.append(
            (name, r'failure', resp_time,)
        )

    async def run(self):
        raise NotImplementedError()