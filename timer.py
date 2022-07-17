import msvcrt
import time
import datetime
import os
import pywinauto

def choiser(t2_):
    print("\n\nPress ENTER for continue")
    print("Press ESC for exit")
    print("Press Z for set counter to zero")
    print("Press C for change counter (+/-) minutes")
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
    while (not msvcrt.kbhit()) or (msvcrt.getwch() != '\r'):
        t2 = time.time()-t1
        t2 = last_time + int(t2)
        t2_format = str(datetime.timedelta(seconds = t2))
        time.sleep(0.1)
        print('\r' + t2_format, end='')
    choiser(t2)

#change position and size of window
handle_ = pywinauto.findwindows.find_windows(active_only=True)[0]
app = pywinauto.application.Application().connect(handle=handle_)
dlg_spec = app.window()
dlg_spec.move_window(x=500, y=500, width=600, height=400, repaint=True)

os.system('color 37')
os.system('cls')
print("Press ENTER for start/pause")
pressedKey = msvcrt.getwch()
if pressedKey == '\r':
    timer_loop(0)