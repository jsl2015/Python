# coding:utf8
# try 的作用是捕获错误，并在捕获到指定错误时执行 except 语句。
try:
	from cStringIO import StringIO
	print 'import success.'
except ImportError:
	from StringIO import StringIO

try:
    from simplejson import json
except ImportError:
	import json

print json.dumps({'python':2.7})