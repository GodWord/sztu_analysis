# -*- coding:utf-8 -*-
__author__ = 'zhoujifeng'
__date__ = '2019/3/8 13:18'

import logging
import time

from django.http import HttpResponse

from apps.sztu_api.models import Click
from apps.utils.timeUtils import TimeUtils

logger = logging.getLogger('sztu')


def click_api(request):
    if request.method == 'GET':
        ip = request.META.get("HTTP_X_FORWARDED_FOR", "")
        if not ip:
            ip = request.META.get('REMOTE_ADDR', "")
        client_ip = ip.split(",")[-1].strip() if ip else ""
        access_time = TimeUtils.get_datetime_by_timestamp(request.GET.get('access_time', default=time.time() * 1000))
        data = {
            'ip': client_ip,
            'url': request.GET.get('url', default=''),
            'dom_name': request.GET.get('dom_name', default=''),
            'access_time': access_time,
        }
        if data['dom_name'] != '':

            logger.info('数据获取成功:[%s]' % (data,))
            logger.info('数据开始保存')

            add = Click(**data)
            add.save()
            logger.info('数据保存完成')
            logger.info(data)
        else:
            logger.info('请求有误，未获取到[dom_name]')

    return HttpResponse('', content_type="image/png")
