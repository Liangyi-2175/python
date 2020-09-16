from com.stress_test import Utils
from com.stress_test.Guardian import Guardian
from com.stress_test.Report import Reporter


class Launcher(_Launcher):
    """
    框架异步启动器
    fork进程，日志打印，事件循环等功能
    """

    def __init__(self,
                 log_file_path=None, log_level=r'INFO', log_file_num_backups=7,
                 process_number=1, process_guardian=None,
                 debug=False
                 ):

        if process_guardian is None:
            process_guardian = Guardian().run  # 将进程守护的run方法传至_Launcher，获取进程号集合

        # 将日志路径、等级、大小，进程数，进程守护等传给_Launcher
        super().__init__(
            log_file_path, log_level, log_file_num_backups,
            process_number, process_guardian,
            debug
        )

    def run(self, func, *args, **kwargs):
        """
        params func: Runner实例对象的run方法，即一次执行多个脚本任务
        """

        if self._process_number > 1:
            # 多进程情况下，报告输出打印在Guardian().run中完成，
            # 注意在实例对象初始化时已经Guardian().run赋给process_guardian属性
            super().run(func, *args, **kwargs)

        else:

            async def _func():

                nonlocal func, args, kwargs

                with Reporter() as reporter:
                    await func(*args, **kwargs)
                    Utils.log.info(f'\n{reporter.get_report_table()}')
                # 单进程情况下，报告输出打印在_func()中完成，

            super().run(_func)