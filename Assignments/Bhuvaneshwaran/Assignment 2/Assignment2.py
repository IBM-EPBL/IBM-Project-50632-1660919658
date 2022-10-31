import random
from time import*
gate=True
def run_city():
  city = input('input the city name')
  print(city)
  print('displaying weather report for:'+city)
  url = 'https://wttr.in/{}'.format(city)
  res = requests.get(url)
  print(res.text)
while(gate):
    temperature = random.randint(0,50)
    humidity = random.randint(10,50)
    if temperature>45 and humidity<50:
        print("Temperature =",temperature,"Humidity =",humidity)
        print("Alert message is Active")
        gate=False
    else:
        print("Temperature =",temperature,"Humidity =",humidity)
    sleep(1);
x=int(input("enter humidity value:"))
y=int(input("enter temperature value:"))
z=print(x,y)
print(z)
if x==36.5:
    print("According to temperature report you are in normal days")
if x<36:
    print("Your temperature is low compare to norml days")
if x>36:
    print("Your temperature is high compare to normal days")
if y==45:
    print("According to humidity report you are in normal place")
if y<45:
    print("Your humidity is low compare to normal days")
if y>45:
    print("Your humidity is high compare to normal days")
while True:
    run_city()
