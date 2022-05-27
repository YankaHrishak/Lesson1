import random
a1 = random.randint(1,10)
r = range(0,10)
it = iter(r)

l = [a1+5*(next(it)) for i in r]
print()
