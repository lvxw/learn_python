# -*- coding: UTF-8 -*-

import re


def test_match():
    string = "hello world meili fengxin hello"
    match = re.match(r"hello", string)
    if match:
        print(match.group(0))


def test_search():
    string = "world meili fengxin hello"
    match = re.search(r'hello', string)
    if match:
        print(match.group(0))


def test_split():
    string = "hello world meili fengxin hello"
    li = re.split(r" ", string)
    for ele in li:
        print(ele)


def test_sub():
    string = "hello world meili fengxin hello"
    new_str = re.sub(r"hello", "你好", string)
    print(new_str)

def test_findall():
    string = "hello world meili fengxin hello"
    li = re.findall(r"hello", string)
    print(li)


def test_finditer():
    string = "hello world meili fengxin hello hello"
    it = re.finditer(r"hello", string)
    for match in it:
        print(match.group())


if __name__ == "__main__":
    # test_match()
    # test_search()
    # test_split()
    # test_sub()
    # test_findall()