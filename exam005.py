data = list(range(1,10))
print(data)

data2 = data[0:5]
print(data2)
print(data[5:8])
print(data[:3])
print(data[3:])  #print(data([3:len(data)])
print(data[:])

# data [2:5] = [100, 200, 300, 400, 500]
data[2:6:2] = [10, 20]
print('data : ', data)

# del data[2:3]
del data[2:5]
print('data : ', data)