import os

from hagworm.extend.interface import RunnableInterface

from com.stress_test import Utils
from com.stress_test.AsyncCirculatorForSecond import AsyncCirculatorForSecond
from com.stress_test.Report import Reporter


class Guardian(RunnableInterface):
    """
    多进程间zmq消息水位设置，进程守护
    """

    async def _do_polling(self, pids, hwm):

        with Reporter() as reporter:

            reporter.set_hwm(hwm)

            async for _ in AsyncCirculatorForSecond():

                for pid in pids.copy():
                    if os.waitpid(pid, os.WNOHANG)[0] == pid:
                        pids.remove(pid)

                if len(pids) == 0:
                    break

            Utils.log.info(f'\n{reporter.get_report_table()}')

    def run(self, pids):

        global HIGH_WATER_MARK

        Utils.run_until_complete(self._do_polling(pids, HIGH_WATER_MARK))