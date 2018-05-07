# -*- coding: UTF-8 -*-

import re

str = "hello world nihao shijie hello"

regObj = re.compile("hello")
match = regObj.match(str)
if match:
    print(match.group(0))



