# coding:utf8

import base64

def safe_b64decode(str):
	if len(str) % 4 != 0:
		str2 = str + (4 - (len(str) % 4)) * '='
		return base64.b64decode(str2)
	else:
		return base64.b64decode(str)

print safe_b64decode('YWJjZA')

