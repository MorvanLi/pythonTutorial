# -*- coding: utf-8 -*-
# @Time    : 2022/7/23 20:52
# @Author  : Li Bo
# @FileName: get_logging.py
# @Software: PyCharm

import logging
import logging.config


def getLogging(confName="applog"):
    logging.config.fileConfig("logging.conf")
    return logging.getLogger(confName)
