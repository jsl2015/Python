
print [ a + b for a in 'ABC' for b in '123']


print [ int(str(a) + str(b) + str(c)) for a in range(1,10) for b in range(10) for c in range(10) if a == c ]
