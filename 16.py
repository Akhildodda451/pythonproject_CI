a, b, c, d, *e, f, g = range(20)
print(len(e))

for i in range(10):
  try:
    if 10 / i == 2.0:
      break
  except ZeroDivisionError:
    print(1)
  else:
    print(2)