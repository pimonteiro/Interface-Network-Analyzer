import os
import threading
from datetime import datetime
import time

def start_pinging():
    threading.Timer(40.0, start_pinging).start() #called every 5 minutes
    
    hostname = "192.168.1.69" #TODO Insert interface ip
    response = os.system("ping -c 3 -W 5 %s" % hostname)   #20 - tempo de espera de resposta
   
    time.sleep(20) #sleep for 140 seconds
    print("Acabou a espera!!")
    if response != 0:
        if (os.system("ping -c 3 -W 5 www.google.pt")) == 0:
            data = open("logs.txt","a")
            print ("Host is not up")
            data.write("Host is not up!!! ---> %s\n" % str(datetime.now()))
            data.close()
        else:
            data = open("logs.txt","a")
            print("No internet connection, check wifi")
            data.write("Network not working. Please check wifi connection ------> %s\n" % str(datetime.now()))
            data.close()

    else:
        data = open("logs.txt","a")
        data.write("--------------Sucess---------------\n")
        data.close()


start_pinging()
