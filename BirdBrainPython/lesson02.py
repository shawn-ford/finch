from BirdBrain import Finch
bird = Finch()

def exercise1():
    print("Distance: ",bird.getDistance())

def exercise2():
  print("Right Light Sensor:",bird.getLight('R'))
  print("Left Light sensor:", bird.getLight('L'))
  print("A Button sensor:",  bird.getButton('A'))
  print("Finch Orientation:", bird.getOrientation())
  print("Right Encoder Type:", bird.getEncoder('R'))

def exercise3():
  print("Right Light Sensor:",type(bird.getLight('R')))
  print("Left Light sensor:", type(bird.getLight('L')))
  print("A Button sensor:",  type(bird.getButton('A')))
  print("Finch Orientation:", type(bird.getOrientation()))
  print("Right Encoder Type:", type(bird.getEncoder('R')))

def exercise4():
    currentDistance = bird.getDistance()
    print(" Current Distance:", currentDistance)
    print(" Current Distance * 2:", currentDistance * 2)
    print(" Current Distance * 4:", currentDistance * 4)



def exercise5():
   leftLightSensor = bird.getLight('L')
   rightLightSensor = bird.getLight('R')
   difference= int(leftLightSensor - rightLightSensor)
   print("Left Light Senor:", leftLightSensor
   print("Right Light Senor:", rightLightSensor
   print("Difference between light sensors:", difference)
      

def exercise6():
    leftLightSensor = bird.getLight('L')
    rightLightSensor = bird.getLight('R')
    difference= int(leftLightSensor - rightLightSensor)
    mean = (rightLightSensor = leftLightSensor) / 2
    print("Left Light Senor:", leftLightSensor
    print("Right Light Senor:", rightLightSensor
    print("Difference between light sensors:", difference)
    print("Light Sensor Average:", mean)

