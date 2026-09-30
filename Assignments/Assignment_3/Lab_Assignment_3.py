import time
from hs3003 import HS3003

sensor = HS3003()

# This gives all the options to choose from
while True:
    print("Please choose from the follow options: ")
    print("T - Temperature")
    print("H - Humidity")
    print("0 - Both")
    
    #This gives the opportunity input T, H, or 0 to get to the next part
    choice = input("Enter your choice of T, H, or 0 here: ")

#This is what the input gives out depending on what is chosen 
    if choice == "T":
        t, h = sensor.read()
        print("Temperature: {:.2f} C".format(t))
    if choice == "H":
        t, h = sensor.read()
        print("Humidity: {:.2f} %" .format(h))
    if choice == "0":
        t, h = sensor.read()
        print("Temperature: {:.2f} C" .format(t))
        print("Humidity: {:.2f} %" .format(h))
        time.sleep(5) #put 5 for 5 seconds so it doesn't repeat so fast