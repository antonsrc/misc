# te_5

from colorama import Fore, Back, Style, init
init()

arr = [15,9,8,1,4,11,7,12,13,6,5,3,16,2,10,14]

print('\narr (before): ', end='')
for j in range(len(arr)):
    print(str(arr[j]) + ' ',end='')
print()

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
        print('\narr (after):  ',end='')
        for j in range(len(arr)):
            if (j == i):
                print(Fore.BLACK + Back.GREEN + str(arr[j]) + ' ', end='')
                print(Style.RESET_ALL, end='')
            else:
                print(str(arr[j]) + ' ', end='')
    i -= 1

