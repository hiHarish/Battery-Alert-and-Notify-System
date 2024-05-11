import psutil
import time
import winsound
from winotify import Notification, audio

def battery_low():
    charge1=battery.percent
    battery1 = psutil.sensors_battery()
    if battery1.power_plugged == False and charge<=30:
        print("Please consider charging")
        low= Notification(app_id="Battery" , title="Charge left: %s %% "%(battery.percent), msg="Consider Charging", duration="long")
        low.show()
        time.sleep(60)
        
def battery_reach_limit():
    charge2=battery.percent
    battery1 = psutil.sensors_battery()
    if  battery1.power_plugged== True and charge>=75 and charge<=77:
        print("remove Charging")
        high=Notification(app_id="Battery", title="Current Charge: %s %% "%(battery.percent), msg="Remove Charging", duration="long")
        high.show()
        winsound.Beep(5000,3000)
        time.sleep(60)
        
while True:
    battery = psutil.sensors_battery()
    charge=battery.percent
    if charge>=75:
        battery_reach_limit()
    elif charge<=30:
        battery_low()
    else:
        time.sleep(300)



            


