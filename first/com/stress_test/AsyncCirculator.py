from com.stress_test import Utils


class AsyncCirculator:
    """异步循环器

    提供一个循环体内的代码重复执行管理逻辑，可控制超时时间、执行间隔(LoopFrame)和最大执行次数

    async for index in AsyncCirculator():
        pass

    其中index为执行次数，从1开始

    """

    def __init__(self, timeout=0, interval=0xff, max_times=0):

        if timeout > 0:
            self._expire_time = Utils.loop_time() + timeout
        else:
            self._expire_time = 0

        self._interval = interval
        self._max_times = max_times

        self._current = 0

    def __aiter__(self):

        return self

    async def __anext__(self):

        if self._current > 0:

            if (self._max_times > 0) and (self._max_times <= self._current):
                raise StopAsyncIteration()

            if (self._expire_time > 0) and (self._expire_time <= Utils.loop_time()):
                raise StopAsyncIteration()

            await self._sleep()

        self._current += 1

        return self._current

    async def _sleep(self):

        await Utils.wait_frame(self._interval)