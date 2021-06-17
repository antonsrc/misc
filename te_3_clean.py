# te_3

# arr = [100, -70, 100, -15, 8.9, 505, 500, 3.1]
f = open('rand_data_10k.txt')
rand_d = f.read()
rand_d = rand_d.split()

arr = []
for i in rand_d:
    arr.append(int(i))

print('arr (before): ',arr)

import time
s_time = time.time()

trig = 1
while(trig == 1):
    trig = 0
    for i in range(len(arr)-1):
        if(arr[i] > arr[i+1]):
            b = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = b
            trig = 1

time_var = time.time() - s_time
print('\narr (after): ',arr)
print('\ntime = ',time_var)
