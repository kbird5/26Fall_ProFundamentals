#### using code from main.py does not help achieve the moving average while printing temp prints. It does create a moving average for t and h though.
#import time
#from hs3003 import HS3003

#sensor = HS3003()


#while True:
  #  t, h = sensor.read()
   # print("Temp: {:.1f} C   Humidity: {:.1f} %".format(t, h))
    #time.sleep(2)
    
#Temp = 22.6
    
    
### This does not help create a moving average
    #Temp = sensor.read()

# if {:.1f} C <20:
#         print("The temperature is low")
# if {:.1f} C >22:
#         print("The temperature is high")
# if {:.1f} C >20 and Temp < 22:
#         print ("The temperature is normal")
        ###This code does not allow for a moving average

#Temp = 21
#if Temp <20:
    #print("The temperature is low")
#if Temp >22:
   # print ("The temperature is high")
#if Temp > 20 and Temp < 22:
    #print ("The temperature is normal")
   
import time
from hs3003 import HS3003

sensor = HS3003()


while True:
    temp0, humid0 = sensor.read()
    print("Temp: {:.1f} C   Humidity: {:.1f} %".format(temp0, humid0))
    time.sleep(2)
    
    temp1, humid1 = sensor.read()
    print("Temp: {:.1f} C   Humidity: {:.1f} %".format(temp1, humid1))
    time.sleep(2)
    
    temp2, humid2 = sensor.read()
    print("Temp: {:.1f} C   Humidity: {:.1f} %".format(temp2, humid2))
    time.sleep(2)
    
    temp3, humid3 = sensor.read()
    print("Temp: {:.1f} C   Humidity: {:.1f} %".format(temp3, humid3))
    time.sleep(2)
    
    temp4, humid4 = sensor.read()
    print("Temp: {:.1f} C   Humidity: {:.1f} %".format(temp4, humid4))
    time.sleep(2)
    
    temp5, humid5 = sensor.read()
    print("Temp: {:.1f} C   Humidity: {:.1f} %".format(temp5, humid5))
    time.sleep(2)
    
    Average_temperature = (temp0+temp1+temp2+temp3+temp4+temp5)/6
    
    print(f"Average_temperature {(temp0+temp1+temp2+temp3+temp4+temp5)/6}")
    
    if (Average_temperature) >20 or (Average_temperature) <22:
        print("The temperature is normal")
    if (Average_temperature) <20:
        print("The temperature is low")
    if (Average_temperature) >22:
        print("The temperature is high")
        
    print(f"Average_humidity {(humid0+humid1+humid2+humid3+humid4+humid5)/6}")
    
    