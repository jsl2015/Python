class Fib(object):

    def __init__(self, num):
        self.num = num
        self.fibo = [0,1]
        i = 2
        while i < self.num:
            self.fibo.append(self.fibo[i-2] + self.fibo[i-1])
            i = i + 1
    
    def __str__(self):
        return str(self.fibo)

    def __len__(self):
        return len(self.fibo)

f = Fib(10)
print f
print len(f)

