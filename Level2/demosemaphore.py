from threading import *
import time
s=Semaphore(3)
def wish(name):
    s.acquire()
    for i in range(10):
        print("good evening",end='')
        time.sleep(2)
        print(name)
    s.release()
t1=Thread(target=wish,args={'jose'})
t2=Thread(target=wish,args={'mart'})
t3=Thread(target=wish,args={'sindhu'})
t4=Thread(target=wish,args={'lavanya'})
t1.start()
t2.start()
t3.start()
t4.start()
