# -*- coding: UTF-8 -*-


# 当异常时，捕获并获取异常
def test1():
    try:
        open("1.tx")
    except IOError:
        print("发生了错误")


# 当异常时，捕获并获取异常对象
def test2():
    try:
        open("1.tx")
    except IOError as errorMsg:
        print("发生了错误", errorMsg)


# 当异常未发生时，执行else语句
def test3():
    try:
        open("2.txt")
    except IOError as errorMsg:
        print("发生了错误", errorMsg)
    else:
        print("没有发生异常")


# 无论是否发生异常,finally语句必执行
def test4():
    try:
        open("2.txt")
    except IOError as errorMsg:
        print("发生了错误", errorMsg)
    else:
        print("没有发生异常")
    finally:
        print("finally语句执行")


# try...finally语句
def test5():
    try:
        open("2.txt")
    finally:
        print("finally语句执行")


# 触发异常raise
def test6():
    raise Exception("触发异常")


test1()
test2()
test3()
test4()
test5()
try:
    test6()
except Exception as errorMsg:
    print(errorMsg)