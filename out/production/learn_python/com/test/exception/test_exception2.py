# -*- coding: UTF-8 -*-


class MyException(Exception):
    def __init__(self, arg):
        self.arg = arg


def test_exception():
    try:
        raise MyException("自定义异常")
    except MyException as errorMsg:
        print(errorMsg.arg)


test_exception()