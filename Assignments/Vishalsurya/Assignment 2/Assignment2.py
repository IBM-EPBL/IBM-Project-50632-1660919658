import datetime
import random,time
x=1
while x==1:
    e = datetime.datetime.now()
    print("Current time: = %s:%s:%s" % (e.hour, e.minute, e.second))
    temp=random.randint(18,50)
    humid=random.randint(60,100)
    print("The temperature is : ",temp)
    print("The humidity is ",humid,"%")
    if temp>=30 or humid>=80:
        if temp>=30:
            print("Temperature is greater than 30 degrees")
        if humid>=80:
            print("The humidity is greater than 80% ")
        if temp>=30 and humid>=80:
            print("The temperature and humidity values exceeds its normal value")
        print("Alarm rings")
    else:
        print("Alarm goes off")
    time.sleep(2)
