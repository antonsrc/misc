# 2

import math
from operator import itemgetter

pts = [
    [5,1],
    [8,3],
    [1,5],
    [-5,9],
    [8,-9],
    [-1,0],
    [-5,-6],
    [5,8],
    [8,8],
    [10,3]]

n = len(pts)

print('pts:')
for i in range(n):
    print(pts[i])

# находим наинизжую точку списка и меняем ее с последней точкой списка
lowest = 0
lowestY = pts[lowest][1]
for i in range(1, n):
    if (pts[i][1] < lowestY):
        lowestY = pts[i][1]
        lowest = i

if (lowest != n-1):
    temp = pts[n-1]
    pts[n-1] = pts[lowest]
    pts[lowest] = temp

print('\npts (after relocation lowest Y at end of list):')
for i in range(n):
    print(pts[i])

# lowest point
baseX = pts[n-1][0]
baseY = pts[n-1][1]

# angle searching
temp_arr = []
for i in range(0, n):
    atn = math.atan2(baseY-pts[i][1],pts[i][0]-baseX)
    temp_arr.append([[pts[i][0]],[pts[i][1]],[atn]])


print('\npts (extended):')
for i in range(n):
    print(temp_arr[i])

pts2 = sorted(temp_arr, key=itemgetter(2,1))

print('\npts (extended and sorted):')
for i in range(n):
    print(pts2[i])

