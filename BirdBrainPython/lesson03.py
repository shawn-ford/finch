from BirdBrain import Finch
from time import sleep
bird = Finch()

def exercise1():
    bird.setBeak(10,5,7)
    sleep(6)
    bird.setBeak(0,0,0)

def exercise2():
    bird.setBeak(100,0,100)
    sleep(3)
    bird.setBeak(0,100,100)
    sleep(3)
    bird.setBeak(100,100,0)
    sleep(2)
    bird.stopAll()

def exercise3():
    bird.setTail(1,0,0,100)
    bird.setTail(4,0,0,100)
    sleep(2)
    bird.stopAll()

def exercise4():
    bird.setBeak(100,0,0)
    bird.setTail(1,100,64,0)
    bird.setTail(2,100,100,0)
    bird.setTail(3,0,100,0)
    bird.setTail(4,0,0,100)
    sleep(5)
    bird.stopAll()

def exercise5():
    userResponse = input("which tail light 1-4 should be red? ")
    number = int(userResponse)
    bird.setTail(number,100,0,0)
    sleep(1)
    bird.stopAll()

def exercise6():
    bird.setTail(all,100,100,100)

exercise6()
