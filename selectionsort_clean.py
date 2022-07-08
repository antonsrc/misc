# arr = [15,9,8,1,4,11,7,12,13,6,5,3,16,2,10,14]
f = open('rand_data_10k.txt')
rand_d = f.read()
rand_d = rand_d.split()

arr = []
for i in rand_d:
    arr.append(int(i))

print('arr (before): ',arr)

import time
s_time = time.time()

def selectMax(arr,left,right):
    maxPos = left
    i = left
    while(i <= right):
        if (arr[i] > arr[maxPos]):
            maxPos = i
        i += 1
    return maxPos

arr_len = len(arr)-1

for i in range(arr_len,0,-1):
    maxPos = selectMax(arr,0,i)
    if (maxPos != i):
        temp = arr[i]
        arr[i] = arr[maxPos]
        arr[maxPos] = temp
    i -= 1

time_var = time.time() - s_time
print('\narr (after): ',arr)
print('\ntime = ',time_var)
