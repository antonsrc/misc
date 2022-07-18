from random import randint

f = open('rand_data_10k.txt', 'w')
for i in range(10000):
    temp = randint(-10000,10000)
    f.write(str(temp)+'\n')

f.close()

f = open('rand_data_10k.txt')
rand_d = f.read()
rand_d = rand_d.split()

arr = []
for i in rand_d:
    arr.append(int(i))

print(arr)