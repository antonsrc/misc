from colorama import Fore, Back, Style, init
init()

arr = [15,9,8,1,4,11,7,12,13,6,5,3,16,2,10,14]

temp = []

print('\narr (before): ', end='')
for j in range(len(arr)):
    print(str(arr[j]) + ' ',end='')
print()

for k in range(1, len(arr)):
    val = arr[k]
    
    i = k-1
    temp.append([])
    
    while ((k-1) >= 0 and arr[k-1] > val):
        arr[k] = arr[k-1]
        
        temp[i].append(k)
        
        k -= 1
    arr[k] = val
    
    print('\narr (after):  ',end='')
    for j in range(len(arr)):
        if (j in temp[i]):
            print(Fore.BLACK + Back.GREEN + str(arr[j]) + ' ', end='')
            print(Style.RESET_ALL, end='')
        else:
            print(str(arr[j]) + ' ', end='')

