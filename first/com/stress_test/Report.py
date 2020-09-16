from hagworm.extend.asyncio.zmq import Subscriber


class Reporter(Subscriber):
    """
    zmq订阅类的子类，捕获消息和生成统计结果终端打印
    """
    class _Report:

        def __init__(self):
            self.success = []
            self.failure = []

    def __init__(self):

        global SIGNAL_PROTOCOL, SIGNAL_PORT, HIGH_WATER_MARK

		# zmq订阅方tcp地址，与发布方对应
        super().__init__(f'{SIGNAL_PROTOCOL}://*:{SIGNAL_PORT}', True)

		# 设置zmq消息通讯水位，到达水位后再由zmq打包发送
        self.set_hwm(HIGH_WATER_MARK)

        self._reports = {}

    async def _message_handler(self, data):
        """
        params data: 即zmq订阅方收到的消息
        """

        for name, result, resp_time in data:
            if name and result in (r'success', r'failure'):
                getattr(self._get_report(name), result).append(resp_time)

    def _get_report(self, name: str) -> _Report:

        if name not in self._reports:
            self._reports[name] = self._Report()

        return self._reports[name]

    def get_report_table(self) -> str:
        """
        生成统计结果终端表
        """

        reports = []

        for key, val in self._reports.items():
            reports.append(
                (
                    key,
                    len(val.success),
                    len(val.failure),
                    r'{:.2%}'.format(len(val.success) / (len(val.success) + len(val.failure))),
                    r'{:.3f}s'.format(sum(val.success) / len(val.success) if len(val.success) > 0 else 0),
                    r'{:.3f}s'.format(min(val.success) if len(val.success) > 0 else 0),
                    r'{:.3f}s'.format(max(val.success) if len(val.success) > 0 else 0),
                )
            )

        return Table.create(
            reports,
            (
                r'EventName',
                r'SuccessTotal',
                r'FailureTotal',
                r'SuccessRatio',
                r'SuccessAveTime',
                r'SuccessMinTime',
                r'SuccessMaxTime',
            ),
            use_ansi=False
        )