import time, functools

def performance(unit):
    def perf_decorator(f):
    	@functools.wraps(f)
        def wrapper(*args, **kw):
            print 'haha'
        return wrapper
    return perf_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial.__name__