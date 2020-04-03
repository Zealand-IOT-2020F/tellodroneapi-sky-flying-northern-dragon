import Drone
import sys
import time

#here you should interact with the drone
print("booting")

drone1 = Drone.Drone('192.1.1.1',8889)

#Diagnostics

drone1.printinfo()

drone1.connect()

drone1.battery()

#Action

drone1.takeOff()

time.sleep(2)

drone1.ascend_alt(20)

time.sleep(2)

drone1.cw(90)

time.sleep(2)

drone1.ccw(90)

time.sleep(2)

drone1.descend_alt(20)

time.sleep(2)

drone1.cw(180)

time.sleep(2)

drone1.ccw(180)

time.sleep(2)

drone1.land()




drone1.battery()

drone1.ftime()