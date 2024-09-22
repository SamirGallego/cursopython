import functools

numbers=[4,5,6,7]

def accum(counter, item):
  print('counter => ',counter)
  print('item => ',item)
  return counter + item


result = functools.reduce(lambda counter, item: counter + item,numbers)
print(result)

resultado = functools.reduce(accum,numbers)
print(resultado)