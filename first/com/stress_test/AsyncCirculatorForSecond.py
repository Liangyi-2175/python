from com.stress_test import Utils
from com.stress_test.AsyncCirculator import AsyncCirculator


class AsyncCirculatorForSecond(AsyncCirculator):

    def __init__(self, timeout=0, interval=1, max_times=0):

        super().__init__(timeout, interval, max_times)

    async def _sleep(self):

        await Utils.sleep(self._interval)