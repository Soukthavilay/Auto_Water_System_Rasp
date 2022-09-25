# import thu vien
# https://github.com/adafruit/Adafruit_Python_DHT.git

import Adafruit_DHT 
print("hello world")
sensorDHT = Adafruit_DHT.DHT11 # chon loai cam bien (DHT11)
DHT_gpio = 17 # khai bao chan cho cam bien DHT

# ham read_retry se thuc hien lap lai 15 lan viec doc du lieu
humidity,temperature = Adafruit_DHT.read_retry(sensorDHT,DHT_gpio)

# cam bien kiem tra du lieu doc duoc hop le hay ko
if(humidity is not None and temperature is not None):
   print("Temp = {0:0.1f}*C Humidity = {1:0.1f}%".format(temperature,humidity))
else:
   print("False to get reading. Try again bro")
