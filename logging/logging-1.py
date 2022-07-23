# -*- coding: utf-8 -*-
# @Time    : 2022/7/23 11:07
# @Author  : Li Bo
# @FileName: logging-1.py
# @Software: PyCharm

from get_logging import getLogging

logger = getLogging()

try:
    int(a)
except Exception as e:
    logger.exception(e)