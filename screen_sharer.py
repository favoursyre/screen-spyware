#I want to create a python script that would help me share screens with other system

#Useful libraries that I would be working with -->
import os
import sys
import socket
import time
from vidstream import StreamingServer, ScreenShareClient
from threading import Thread
import ip_info


#Declaring the various classes
class ScreenSharer:
    def __init__(self):
        self.user, self.host, self.publicIP, self.privateIP = ip_info.main()
        self.port = 3415

    #This function helps with receiving the video stream
    def receiver(self, host):
        recv = StreamingServer(f"{host}", self.port)
        print(f"Listening on {host}:{self.port}\n\nPress RELEASE when you're ready to end the session")
        t = Thread(target = recv.start_server)
        t.start()

        while input("") != "RELEASE":
            continue

        recv.stop_server()
        return

    #This checks to see if there's a connection on a particular port of the target system
    def connection(self, target):
        time.sleep(10)
        #while True:
        try:
            socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_.connect((target, 6666))
            stat = True
        except:
            stat = False
            raise ConnectionError("The connection got disconnected")
            #break
        finally:
            print(f"Stat: {stat}")
            return stat

    #This function helps with the sending of the video stream
    def sender(self, addr = None):
        if addr:
            pass
        else:
            addr = f"{self.privateIP}"
        
        send = ScreenShareClient(addr, self.port)
        print(f"Connected to {addr}:{self.port}")
        t = Thread(target = send.start_stream)
        t.start()

        #This checks if the connection is still on and terminates it if its disconnected
        while self.connection(addr) != False:
            continue

        send.stop_stream()
        
        return

if __name__ == "__main__":
    print("Screen Sharer\n")

    share = ScreenSharer()
    share.receiver()

    print("\nExecuted successfully!!")