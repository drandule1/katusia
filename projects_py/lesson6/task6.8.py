#Дан список чисел и на вход поступает число N, необходимо сместить список на
#указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]


n=5
data=[1,2,3,4,5,6,7,8]

n=n%len(data)

print(data[-n:])
print(data[0:-n])

data1=data[-n:]+data[0:-n]
print(data1)