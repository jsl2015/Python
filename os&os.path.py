# coding:utf8
#编写一个search(s)的函数，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，
#并打印出完整路径：

#$ python search.py test
#unit_test.log
#py/test.py
#py/test_os.py
#my/logs/unit-test-result.txt

import os

def search(s,jsl):
	for x in os.listdir(jsl):
		if os.path.isfile(x):
			if str(s) in os.path.split(x)[1]:
				mydir = os.path.abspath(jsl)
				myname = os.path.split(x)[1]
				print(os.path.join(mydir, myname))
		if os.path.isdir(os.path.join(jsl,x)):
			search(s,os.path.join(jsl,x))

print search('a','.')


			