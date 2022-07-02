# te_9

import msvcrt
import time
import datetime

def choiser(t2_):
    print("\n\nPress ENTER for continue")
    print("Press ESC for exit")
    print("Press Z for set counter to zero")
    print("Press C for change counter (+/-) seconds")
    inp = msvcrt.getwch()
    if (inp == '\r'):       # Enter
        timer_loop(t2_)
    elif (inp == '\x1b'):   # Esc
        print("Exit")
    elif (inp == 'z'):
        timer_loop(0)
    elif (inp == 'c'):
        t3 = int(input())
        t3 *= 60
        timer_loop(t2_+t3)
    else:
        choiser(t2_)

def timer_loop(last_time):
    t1 = time.time()
    i = 1
    while (not msvcrt.kbhit()) or (msvcrt.getwch() != '\r'):
        time.sleep(0.1)
        t2 = time.time()-t1
        t2 = last_time + int(t2)
        t2_format = str(datetime.timedelta(seconds = t2))
        if t2 >= i: 
            print('\r' + t2_format, end='')
            i += 1
    choiser(t2)

print("Press ENTER for start/pause")
pressedKey = msvcrt.getwch()
if pressedKey == '\r':
    timer_loop(0)