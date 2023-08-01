from datetime import datetime
from threading import Timer

print ("Введите время: чч:мм")
wakeUptime = str(input())
i = 0
stopThread = False
print('Будильник установлен на '+ wakeUptime)

def alarmClock():
    global wakeUptime
    global i
    global stopThread
    if not stopThread:
        now = datetime.now()
        timeNow = str(now.time())[0:5]
        Timer(10, alarmClock).start()
        print(timeNow)
        if timeNow >= wakeUptime:
            print('Пора вствать!')
            if (i == 2):
                print("Молодец!!!")
                stopThread = True
            i += 1     

alarmClock()
