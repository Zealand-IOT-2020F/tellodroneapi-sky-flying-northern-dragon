import threading 
import socket
import sys
import time

host = ''
port = 9000
locaddr = (host,port) 

#UDP Link
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)




class Drone(object):
    """description of class"""

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

#Startup/shutdown

    def connect(self)
        print("command interface initializing")
        result = self.sendMessage("command")
        print (result)
    def end(self):
        print("end")
        self.sock.close()


#Takeoff/Landing

    def takeOff(self):
        print("takeOff")
        result = self.sendMessage("takeoff")

    def land(self)
        print("Landing")
        result = self.sendMessage("land")

    def stop(self)
        print("Stopping")
        result = self.sendMessage("stop")
    
    def HALT(self)
        print("AAAAAAAAH *PANTS ON HEAD* *HEADLESS CHICKEN*")
        result = self.sendMessage("emergency")


#Diagnostics

    def battery(self)
        print("Battery level in %: ")
        result = self.sendMessage("battery?")
    
    def qspeed(self)
        print("speed is set at: ")
        result = self.sendMessage("speed?")

    def ftime(self)
        print("Drone has flown for: ")
        result = self.sendMessage("time?")

#Flightcontrols

    def cw(self,x):
        print("cw")
        r = self.sendMessage("cw "+x)

    def ccw(self,x):
        print("ccw")
        r = self.sendMessage("ccw "+x)

    def ascend_alt(self,x)
        print("Ascending to "+x)
        result = self.sendMessage("up "+x)
    
    def descend_alt(self,x)
        print("Descending to "+x)
        result = self.sendMessage("down "+x)
    
    def forward(self,x)
        print("Moving forward "+x)
        result = self.sendMessage("forward "+x)
    
    def backwards(self,x)
        print("Moving backwards"+x)
        result = self.sendMessage("back "+x)
    
    def left(self,x)
        print("Moving left"+x)
        result = self.sendMessage("left "+x)

    def right(self,x)
        print("Moving right"+x)
        result = self.sendMessage("right "+x)
    
    