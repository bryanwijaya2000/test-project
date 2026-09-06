from utils import add, subtract

def foo(a, b):
  if add(a, b) + subtract(a, b) == 0:
    return 0
  if add(a, b) > 0:
    return 1
  if subtract(a, b) < 0:
    return -1
  return 1000

print(foo(10, 9))
print(foo(20, 100))
