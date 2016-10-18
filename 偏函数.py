# encoding:utf8
# 偏函数：减少参数个数，就可以简化调用者的负担

def int2(x, base=2):
    return int(x, base)

print int2('11111111')

import functools

int3 = functools.partial(int, base=2)

print int3('10000000')

import functools

sorted_ignore_case = functools.partial(sorted, key = str.lower)

print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])