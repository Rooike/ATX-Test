#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
from Public.ReadConfig import ReadConfig

proDir = os.path.split(os.path.realpath(__file__))[0]
data_path = os.path.join(proDir, "data.json")


def get_json_path():
    return data_path


# 取需要执行的函数名
def get_exec_func():
    return ReadConfig().get_config_func()


# 执行函数
def exec_func(func, *args):
    if args:
        exec("{}({})".format(func, args))
    else:
        exec("{}()".format(func))


# 写json装饰器
def decorator_gen_data_func(func):
    def wrapper(*args):
        res = func(*args)
        with open(data_path, "w", encoding='UTF-8') as f:
            json.dump(res, f, ensure_ascii=False)
            f.close()
        print("Test data data.json generated success")

    return wrapper


# 获取需要爬取的城市列表
@decorator_gen_data_func
def get_splider_city_list():
    city_list = ReadConfig().get_citys_list('city_list')
    return city_list


# if __name__ == '__main__':
#     func = get_exec_func()
#     paths = get_json_path()
#     get_splider_city_list()
