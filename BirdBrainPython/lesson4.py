from BirdBrain import Finch
import time 

finch = Finch()

def exercise1():
    finch.setMotors(50, 50)
    time.sleep(1)
    finch.stopAll()

def exercise2():
    rightWheelSpeed = int(input('Whats the right wheel speed'))
    leftWheelSpeed = int(input('Whats the left wheel speed'))
    finch.setMotors(leftWheelSpeed, rightWheelSpeed)
    time.sleep(2)
    finch.stopAll()

def exercise3():
    finch.setMotors(0, 25)
    time.sleep(3)
    finch.stopAll()
    finch.setMove('F', 25, 24)
    finch.setMotors(25, 0)
    time.sleep(4)
    finch.stopAll()
    finch.setMove('F', 25, 24)

def exercise4():
    color = input('Please enter a letter:')
    if (color =='g'):
        finch.setBeak(0,100,0)
    else:
        print('Sorry, that is not y favorite letter!')
        sleep(1)
        finch.stopAll()

def exercise5():
    turnInput = str(input(" Enter \'r\' for a right turn or \'l\' for a left turn"))
    if(turnInput == 'r' or turnInput == 'R'):
        print("Turning Right!")
        finch.setMotors(25, 0)
        time.sleep(3)
        finch.stopAll()
    elif(turnInput == 'l' or turnInput == 'L'):
        print("Turning Left!")
        finch.setMotors(0, 25)
        time.sleep(3)
        finch.stopAll()
    else:
        print("invalid Input, termanating program")

def exercise6():
    speed= int(input("Enter a speed between -100 and 199: "))
    if(speed >= -110) and (speed <= 100):
        print("Moving finch at ()% speed!".format(speed))
        finch.setMotor(speed, speed)
        time.sleep(1)
        finch.stopAll()
    else:
        print("That speed is not valid terminating program")


def exercise7():
    wheelSpeed = int(input('Whats the wheel speed (0-50)'))
    if(wheelSpeed >50 or wheelSpeed <0):
       print("Numbers not valid")
    else:
        finch.setMotors(wheelSpeed, 2*wheelSpeed)
        time.sleep(5)
        finch.stopAll()
    
exercise7()
