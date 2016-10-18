#! coding:utf8

from collections import namedtuple
point = namedtuple('point', ['x', 'y']) # point为命名元组的名称，x、y为2个元素
p = point(1,2)
print p.x
print p.y

