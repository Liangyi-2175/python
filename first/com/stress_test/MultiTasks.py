import asyncio

from com.stress_test import Utils


class MultiTasks:
    """多任务并发管理器

    提供协程的多任务并发的解决方案

    tasks = MultiTasks()
    tasks.append(func1())
    tasks.append(func2())
    ...
    tasks.append(funcN())
    await tasks

    多任务中禁止使用上下文资源共享的对象(如mysql和redis等)
    同时需要注意类似这种不能同时为多个协程提供服务的对象会造成不可预期的问题

    """

    def __init__(self, *args):

        self._coro_list = list(args)
        self._task_list = []

    def __await__(self):

        if len(self._coro_list) > 0:
            self._task_list = [Utils.create_task(coro) for coro in self._coro_list]
            self._coro_list.clear()
            yield from asyncio.gather(*self._task_list).__await__()

        return [task.result() for task in self._task_list]

    def __len__(self):

        return self._coro_list.__len__()

    def __iter__(self):

        for task in self._task_list:
            yield task.result()

    def __getitem__(self, item):

        return self._task_list.__getitem__(item).result()

    def append(self, coro):

        return self._coro_list.append(coro)

    def extend(self, coro_list):

        return self._coro_list.extend(coro_list)

    def clear(self):

        self._coro_list.clear()
        self._task_list.clear()