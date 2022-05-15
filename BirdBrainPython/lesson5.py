from BirdBrain import Finch
import time 

finch = Finch()


def exercise1():
    if finch.getButton('A') or finch.getButton('B'):
       finch.setBeak(0,100,0)
    else:
        finch.setBeak(100,0,0)
    time.sleep(1)
    finch.stopAll()

def exercise2():
    if finch.getButton('B'):
        finch.setMove('B',15,10)
    else:
        finch.setMove('F',16,10)       
    
def exercise3():
    print(finch.getDistance())
    if finch.getDistance() <30:
        finch.setTail("all",0,0,100)
    else:
        finch.setTail("all",100,0,0)
    time.sleep(2)
    finch.stopAll()

def exercise4():
    if finch.getDistance()> 200:
        finch.setMove('F',16,10)
    else:
        finch.setMove('B',16,10)

def exercise5():
    while finch.getDistance() <30:
        finch.setBeak(100,0,0)
    finch.setBeak(0,100,0)
    time.sleep(1)
    finch.stopAll()

def exercise6():
    finch.Move('F',40,100)


def exercise7():
    while finch.getDistance() > 20:
        finch.setTail("all",0,0,100)
        time.sleep(3)
        finch.setTail("all",100,0,100)
        time.sleep(3)
        finch.stopAll

def exercise8():
     print(finch.getDistance())
    while finch.getDistance() >30:
        finch.setTail("all",100,0,0)
        finch.setBeak(100,0,0)
        time.sleep(2)
        finch.setTail("all",0,0,0)
        finch.setBeak(0,0,0)
        time.sleep(2)
    else:
        finch.setTail("all",100,0,0)
        time.sleep(2)
        finch.setTail("all",100,50,8)
        fich.setMove("F",15,10)
        finch.setTurn("R",40,10)
        finch.stopAll()

def exercise9():
    while not finch.getButton('A'):
         finch.setTail(1,0,100,0)
         time.sleep(0.1)
         finch.setTail(3,0,100,0)
         time.sleep(0.1)
         finch.stopAll()
         time.sleep(0.1)

def exercise10():
    while not finch.getButton('B'):
        finch.setMove("F",10,10)
        finch.setMove("B",10,10)

def exercise11():        
     finch.setBeak(100,0,0)
     while finch.getDistance() < 30:
         pass
     finch.setBeak(0,100,0)
     time.sleep(1)
     finch.stopAll()

def exercise12():
     print(finch.getDistance())
    while finch.getDistance() >30:
        finch.setTail("all",100,0,0)
        finch.setBeak(100,0,0)
        time.sleep(2)
        finch.setTail("all",0,0,0)
        finch.setBeak(0,0,0)
        time.sleep(2)
