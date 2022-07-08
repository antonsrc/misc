from colorama import Fore, Back, Style, init
init()

arr = [100, -70, 100, -15, 8.9, 505, 500, 3.1]

print('\narr (before): ', end='')
for j in range(len(arr)):
    print(str(arr[j]) + ' ',end='')
print()

counter = 0
trig = 1
while(trig == 1):
    trig = 0
    for i in range(len(arr)-1):
        if(arr[i] > arr[i+1]):
            b = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = b
            trig = 1
            counter += 1
            
            print('\narr (after):  ', end='')
            for j in range(len(arr)):
                if (j == i) or (j == i+1):
                    print(Fore.BLACK + Back.GREEN + str(arr[j]) + ' ', end='')
                    print(Style.RESET_ALL, end='')
                else:
                    print(str(arr[j]) + ' ', end='')

