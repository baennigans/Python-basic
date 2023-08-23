data = [10, 20, 30 ,40, 'hello']
print(type(data), data)
data = list()
print(type(data), data)

data = (10, 20, 30 ,40, 'hello')
print(type(data), data)
data = tuple()
print(type(data), data)

data = range(10)
print(type(data), data)
data = list(data)
print(data)

data = range(5, 15)
print(list(data))

data = list(range(1, 10, 2))
print(data)