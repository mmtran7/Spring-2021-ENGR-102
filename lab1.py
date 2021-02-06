### LAB 1, Mahal Tran, ENGR 102

## 1. Start up PyCharm & create a new file called lab1.py

## 2. Add variables for fallingTime, acceleration, and ESBHeight.

fallingTime = 0
acceleration = 9.8
ESBHeight = 381

## 3. Write an expression that computes fallingTime.

import math
fallingTime = math.sqrt(2 * ESBHeight / acceleration)


### 4. Add a print statement that displays your answer.
# It should print: "It takes X seconds to reach the ground."

print("It takes %f seconds to hit the ground." % fallingTime)

# So how fast is the penny moving at this point?
# velocity = time * acceleration.
### 5. Write an expression for this & a print statement that displays the velocity.
velocity = fallingTime * acceleration
print("The penny's velocity is %f m/s." % velocity)

### 6. How long will this take? Create a variable called timeToTerminalVelocity, & an expression that computes this.
# 18 m/s is terminal velocity.

timeToTerminalVelocity = 18 / acceleration

### 7. How far will the penny fall during this period?
## Create a variable called accelDistance & an expression that computes it.
## distance = acceleration * time^2 / 2

accelDistance = acceleration * timeToTerminalVelocity ** 2 /2

### 8. How long will it take to fall the remaining distance?
# Create a variable called timeAtTerminalVelocity & an expression that computes it.

timeAtTerminalVelocity = (ESBHeight - accelDistance)  / 18
print("Time at terminal velocity is %a seconds." % timeAtTerminalVelocity)

def increment(inputVar) :
    return inputVar + 1

### 9. Make a function called fallingTime. It should take one parameter,
# called fallingDistance as input, and return  the time needed to fall a
# given distance, according to the expression above

def fallingTime(fallingDistance) :
    fallTime = math.sqrt(2 * fallingDistance / acceleration)
    print ("Falling time is %f seconds." % fallTime)
    return fallTime


### 10. What if we decide to visit other planets?
## 9.8 m/s^2 is Earth's gravitational force at sea level
### on the moon: 1.6 m/s^2
### on mars: 3.69 m/s^2
### on jupiter: 24.79 m/s^2
### on saturn: 10.44 m/s^2
### on titan: 1.4 m/s^2
### on venus: 8.87 m/s^2


### 10. Make a function called spaceFallingTime that takes two parameters:
## a distance & local acceleration, returns elapsed time

def spaceFallingTime(fallingDistance, localAcceleration) :
    fallTime = math.sqrt(2 * fallingDistance / localAcceleration)
    print ("Falling time with acceleration of %f m/s^2 is %f seconds." % (localAcceleration, fallTime))
    return fallTime

### OMIT 11.

### 12. Remember how programmers are lazy?
## Let's make helper function getAcceleration using a conditional statement
### 13. What if the user asks for a planet we don't know?

## spaceEntity is a string that tells us where we are.
def getAcceleration(spaceEntity) :
    if spaceEntity == "earth" :
        return 9.8
    elif spaceEntity == "moon" :
        return 1.6
    elif spaceEntity == "mars" :
        return 3.69
    elif spaceEntity == "jupiter" :
        return 24.79
    elif spaceEntity == "saturn" :
        return 10.44
    elif spaceEntity == "titan" :
        return 1.4
    elif spaceEntity == "venus" :
        return 8.87
    else :
        return 1.0

def spaceFalling(distance, celestialBody) :
    localAcceleration = getAcceleration(celestialBody)
    localTime = spaceFallingTime(distance, localAcceleration)
    print ("Time fallen on %s is %f seconds." % (celestialBody, localTime))
    return localTime

### Finally, let's deal with air resistance properly. We said that the penny reached terminal velocity at 18 m/s, but not why. Let's model this a little more precisely.
## the penny is subject to two forces: gravity, pulling it down, and air resistance, pushing it up.
## Recall from Newton's second law that F = m * a. Alternatively, a = F / m.
## Weight is defined as m * g. (m is mass, and g gravitational acceleration.)
## The upward force created by air resistance is defined as:
### D = C * 0.5 * r * v^2 * A
## where D is the drag, C is a drag coefficient which represents how easily different shapes cut through a fluid,
## r represents the air density, v the velocity, and A is the cross-sectional area of the object.
### Let's assume that r = 1.29, C = 1.17. and A = 2.85 cm^2.

### First, write a function called pennyDrag.
# It will take as input a velocity, and compute D (drag) using the formula above.

def pennyDrag(velocity) :
    C = 1.17
    r = 1.29
    pennyArea = 2.85
    return C * 0.5 * r * velocity ** 2 * pennyArea

### Next, let's write a function called pennyWeight.
## This will convert mass to weight, using the gravitational acceleration. (9.8m/s^2 on earth.)
# We'll add a default parameter called location, with the default value of Earth.

def pennyWeight(mass, celestialBody="earth") :
    localAcceleration = getAcceleration(celestialBody)
    return mass * localAcceleration


def netForce(mass, velocity, celestialBody="earth") :
    return pennyWeight(mass,celestialBody) - pennyDrag(velocity)


### velocity = sqrt(2 * weight / r * A C)

def terminalVelocity(mass) :
    C = 1.17
    r = 1.2
    pennyArea = 2.83
    weight = pennyWeight(mass)
    tv = math.sqrt(2 * weight / r * pennyArea * C)
    return tv
