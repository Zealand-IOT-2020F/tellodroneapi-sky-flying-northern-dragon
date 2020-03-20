import threading 
import socket
import sys
import time

#host = ''
#port = 9000
#locaddr = (host,port) 

#UDP Link
#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#tello_address = ('192.168.10.1', 8889)

#sock.bind(locaddr)




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
        #print("returværdi")
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
    
    def qspeed(self):
        print("speed is set at: ")
        result = self.sendMessage("speed?")

    def ftime(self):
        print("Drone has flown for: ")
        result = self.sendMessage("time?")
#endregion


#region Flightcontrols

    def cw(self,x):
        if (x >= 1 and x <= 360):
            result = self.sendMessage("cw "+x)
            print("Rotating Clockwise"+x)
        else:
            print("X has to be between 1-360")

    def ccw(self,x):
        if (x >= 1 and x <= 360):
            result = self.sendMessage("ccw "+x)
            print("Rotating Counterclockwise"+x)
        else:
            print("X has to be between 1-360")

    def ascend_alt(self,x):
        if (x >= 20 and x <= 500):
            result = self.sendMessage("up "+x)
            print("Ascending to "+x)
        else:
            print("X has to be between 20-500")
    
    def descend_alt(self,x):
        if (x >= 20 and x <= 500):
            result = self.sendMessage("down "+x)
            print("Descending to "+x)
        else:
            print("X has to be between 20-500")
    
    def forward(self,x):
        if (x >= 20 and x <= 500):
            result = self.sendMessage("forward "+x)
            print("Moving forward "+x)
        else:
            print("X has to be between 20-500")
    
    def backwards(self,x):
        if (x >= 20 and x <= 500):
            result = self.sendMessage("back "+x)
            print("Moving backwards "+x)
        else:
            print("X has to be between 20-500")
   
    def left(self,x):
        if (x >= 20 and x <= 500):
            result = self.sendMessage("left "+x)
            print("Moving left "+x)
        else:
            print("X has to be between 20-500")

    def right(self,x):
        if (x >= 20 and x <= 500):
            result = self.sendMessage("right "+x)
            print("Moving right "+x)
        else:
            print("X has to be between 20-500")
#endregion


#Advanced flightcontrols
