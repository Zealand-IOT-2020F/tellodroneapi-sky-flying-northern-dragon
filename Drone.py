import socket
import sys
import time

class Drone(object):
    """description of class"""
#region Setup
    def __init__(self, ip,port):
        self.TelloIp = ip
        print("ip: " + ip)
        self.TelloPort = port
        # Create a UDP socket
        self.Host =''
        self.HostPort = 9000
        self.locaddr = (self.Host,self.HostPort)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.tello_address = ('192.168.10.1', 8889)
        self.sock.bind(self.locaddr)

    
    def sendMessage(self,TelloMessage):
        print("send message "+ TelloMessage +" end")
        msg = TelloMessage.encode(encoding="utf-8")
        sent = self.sock.sendto(msg,self.tello_address)
        data, server = self.sock.recvfrom(1518)
        #print("returvaerdi")
        print(data.decode(encoding="utf-8"))

        return "from sendmessage " + TelloMessage + " end "
#endregion


#region Startup/shutdown

    def connect(self):
        print("command interface initializing")
        result = self.sendMessage("command")
        print (result)

    def end(self):
        print("end")
        self.sock.close()
#endregion


#region Takeoff/Landing

    def takeOff(self):
        print("Taking off")
        result = self.sendMessage("takeoff")

    def land(self):
        print("Landing")
        result = self.sendMessage("land")

    def stop(self):
        print("Stopping")
        result = self.sendMessage("stop")
    
    def HALT(self):
        print("AAAAAAAAH *PANTS ON HEAD* *HEADLESS CHICKEN* Gentlemen it's been an honor...")
        result = self.sendMessage("emergency")
#endregion


#region Diagnostics

    def battery(self):
        print("Battery level in %: ")
        result = self.sendMessage("battery?")
        return result
    
    def qspeed(self):
        print("speed is set at: ")
        result = self.sendMessage("speed?")
        return result

    def ftime(self):
        print("Drone has flown for: ")
        result = self.sendMessage("time?")
        return result

    def printinfo(self):
        print("Hello Drone at: "+ self.TelloIp)

#endregion


#region Flightcontrols

    def cw(self,x):
        if (x >= 1 and x <= 360):
            result = self.sendMessage("cw " + str(x))
            print("Rotating Clockwise" + str(x))
        else:
            print("X has to be between 1-360")

    def ccw(self,x):
        if (x >= 1 and x <= 360):
            result = self.sendMessage("ccw " + str(x))
            print("Rotating Counterclockwise" + str(x))
        else:
            print("X has to be between 1-360")

    def ascend_alt(self,x):
        if (x >= 20 and x <= 500):
            result = self.sendMessage("up " + str(x))
            print("Ascending to " + str(x))
        else:
            print("X has to be between 20-500")
    
    def descend_alt(self,x):
        if (x >= 20 and x <= 500):
            result = self.sendMessage("down " + str(x))
            print("Descending to " + str(x))
        else:
            print("X has to be between 20-500")
    
    def forward(self,x):
        if (x >= 20 and x <= 500):
            result = self.sendMessage("forward " + str(x))
            print("Moving forward " + str(x))
        else:
            print("X has to be between 20-500")
    
    def backwards(self,x):
        if (x >= 20 and x <= 500):
            result = self.sendMessage("back " + str(x))
            print("Moving backwards " + str(x))
        else:
            print("X has to be between 20-500")
   
    def left(self,x):
        if (x >= 20 and x <= 500):
            result = self.sendMessage("left " + str(x))
            print("Moving left " + str(x))
        else:
            print("X has to be between 20-500")

    def right(self,x):
        if (x >= 20 and x <= 500):
            result = self.sendMessage("right " + str(x))
            print("Moving right " + str(x))
        else:
            print("X has to be between 20-500")
#endregion


#Advanced flightcontrols
