def fib(x):
  if x == 0 or x == 1:
    return 1
  else:
    return fib(x-1) + fib(x-2)
print(fib(4))

from itertools import product
a={1, 2}
print(len(list(product(range(3), a))))


