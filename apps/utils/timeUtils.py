# -*- coding:utf-8 -*-
import time
from datetime import datetime, timedelta

__author__ = 'zhoujifeng'
__date__ = '2019/3/8 16:20'


class TimeUtils:
    @staticmethod
    def get_datetime_by_timestamp(time_stamp):
        """
        将时间戳转换为datetime类型
        :param time_stamp: 时间戳(可能是时间戳字符串)
        :return: datetime
        """
        try:
            if isinstance(time_stamp, str):
                time_stamp = int(time_stamp)
            the_current_time = datetime.fromtimestamp(time_stamp / 1000)
            if the_current_time > datetime.now() or the_current_time < datetime.now() - timedelta(days=1):
                res = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            else:
                res = the_current_time.strftime('%Y-%m-%d %H:%M:%S.%f')
        except Exception:
            res = time.strftime('%Y-%m-%d %H:%M:%S.%f')
        return res
