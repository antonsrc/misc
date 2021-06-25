# te_6

import time
import datetime
from colorama import Fore, Back, Style, init
init()

input('comment: ')
STOP_TIME = input('time in h m or/and s: ')
STOP_TIME = STOP_TIME.split(' ')

stop_s = 0
stop_m = 0
stop_h = 0

for i in list(STOP_TIME):
    if 's' == i[-1:]:
        stop_s = int(i[0:-1])
    if 'm' == i[-1:]:
        stop_m = int(i[0:-1])*60
    if 'h' == i[-1:]:
        stop_h = int(i[0:-1])*60*60

START_TIME = time.time()
STOP_TIME = stop_s + stop_m + stop_h

while (True):
    dif = time.time() - START_TIME
    time.sleep(1)
    print(datetime.timedelta(seconds = int(dif)),'\r',end='')
    
    if (dif >= STOP_TIME):
        now = datetime.datetime.now()
        now = str(now.hour)+':'+str(now.minute)+':'+str(now.second)
        print('\n'+Fore.BLACK+Back.GREEN+'end at '+now+Style.RESET_ALL)
        break
