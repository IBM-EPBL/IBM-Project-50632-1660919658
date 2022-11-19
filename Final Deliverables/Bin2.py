import time
import random
import sys
import requests 
import json
import ibmiotf.application
import ibmiotf.device


# watson device details

organization = a7g2jo
devicType =  Garbage-Bin
deviceId = Garbage_Bin-II
authMethod= token
authToken= Cs_e4IG2RBps4cAMxe

#generate random values for random variables (Distance and load)



def myCommandCallback(cmd)
    global a
    print(command recieved%s %cmd.data['command'])
    control=cmd.data['command']
    print(control)

try
        deviceOptions={org organization, type devicType,id deviceId,auth-methodauthMethod,auth-tokenauthToken}
        deviceCli = ibmiotf.device.Client(deviceOptions)
except Exception as e
        print(caught exception connecting device %s %str(e))
        sys.exit()

#connect and send a datapoint Distance with value integer value into the cloud as a type of event for every 10 seconds
deviceCli.connect()

while True
    lat= 32.939021
    lon= 75.135731
    location= Thiruparankundram, Madurai, Tamil Nadu, India
    Distance= random.randint(1,75)
    Loadcell= random.randint(0,20)
    data= {'dist'Distance,'load'Loadcell,'Latitude'lat,'Longitude'lon,'Location'location}
    if Loadcell5 and Loadcell0
        load=20%
    elif Loadcell10 and Loadcell5
        load=40%
    elif Loadcell15 and Loadcell10
        load=60%
    elif Loadcell18 and Loadcell15
        load=80%
    elif Loadcell20 and Loadcell18
        load=90%
    else
        load=100%
	
    if Distance7 and Distance1
        level=90%
    elif Distance15 and Distance7
        level=80%
    elif Distance30 and Distance15
        level=60%
    elif Distance45 and Distance30
        level=40%
    elif Distance60 and Distance45
        level=20%
    elif Distance75 and Distance60
        level=10%
    else
        level=0%

    if level==90% or load==90%
          warn = 'alert''Dustbin is almost filled in latitude32.939021 and longitude75.135731 Thiruparankundram, Madurai, Tamil Nadu, India'
    
    def myOnPublishCallback(latitude=32.939021,longitude=75.135731 )
        print(Thiruparankundram, Madurai, Tamil Nadu, India)
        print(published Level of bin = %s  %level,Load = %s  %load, Latitude = %s  %latitude,Longitude = %s  %longitude)
        print(load)
        print(level)
        print(warn)
        
    time.sleep(10)
   
   
    success=deviceCli.publishEvent (IoTSensor,json,warn,qos=0,on_publish= myOnPublishCallback)
   
    success=deviceCli.publishEvent (IoTSensor,json,data,qos=0,on_publish= myOnPublishCallback)
   
    

    if not success
        print(not connected to ibmiot)
    time.sleep(20)
   
           
   

    deviceCli.commandCallback=myCommandCallback
#disconnect the device
deviceCli.disconnect()
