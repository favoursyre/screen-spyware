#I want to create a script that gets the private and public ip address

#Useful libraries that I would be working with -->
import socket
import os
import time
import traceback
import urllib.request

#Commencing with the code -->
def main():
    #This retries getting the IP infos incase there's a network error
    while True:
        try:
            try:
                user = os.path.expanduser('~').split('\\')[2]
            except:
                user = "Null"
            hostname = socket.gethostname()
            publicIP = urllib.request.urlopen('https://api.ipify.org/').read().decode('utf8')
            privateIP = socket.gethostbyname(socket.gethostname())
            break
        except:
            print(f"An error occurred in ip_info due to {traceback.format_exc()} \nTrying again")
        time.sleep(5)

    return user, hostname, publicIP, privateIP

if __name__ == "__main__":
    print("IP INFO \n")

    user, hostname, publicIP, privateIP = main()
    print(f"Username: {user}")
    print(f"Hostname: {hostname}")
    print(f"Public IP: {publicIP}")
    print(f"Private IP: {privateIP}")

