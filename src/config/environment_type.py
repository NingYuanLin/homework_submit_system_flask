#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/6/1 5:11 下午
# @Author : lin
# @File : environment_type.py
# @version : v1.0
# @editor : lin
# @desc : 功能模块 功能概述
import enum


class EnvType(enum.Enum):
    DEV = 0  # 开发(测试)
    RELEASE = 1  # 正式


_NOW_ENV = EnvType.DEV
print('当前全局环境：{}'.format(_NOW_ENV.name))


def get_env_type():
    return _NOW_ENV
