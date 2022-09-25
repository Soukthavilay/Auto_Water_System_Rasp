import RPi.GPIO as gp
import pyrebase
config={
    "apiKey": "AIzaSyDdyyHsdfLljDDqcGmBLhqavO3Hb9ywp-U",
    "authDomain": "pbl5-rasberry.firebaseapp.com",
    "databaseURL": "https://pbl5-rasberry-default-rtdb.firebaseio.com",
    "projectId": "pbl5-rasberry",
    "storageBucket": "pbl5-rasberry.appspot.com",
    "messagingSenderId": "50063191700",
    "appId": "1:50063191700:web:369c8c390d8775e92d4e81"
        
}
gp.setmode(gp.BOARD)  
gp.setup(8,gp.IN)  
gp.setup(12,gp.OUT, initial=gp.LOW)  
gp.setup(26,gp.OUT,initial=gp.LOW)  
gp.setup(32,gp.OUT,initial=gp.LOW)

firebase = pyrebase.initialize_app(config)
db = firebase.database()

manual= false;
water_pump= false


# water_pump = db.child("water_pump").get().val()

while True:
    try:
     manual =db.child("manual").get().val()
     if not manual:
      status= not gp.input(8)
      status= not status
      print(status)  
      #gp.output(36,gp.input(8))  
      gp.output(32,not gp.input(8))  
      gp.output(12, status)
      data = {"water_pump": status}
      db.child("").child().update(data)
     else:
      status= db.child("water_pump").get().val()
      gp.output(12, status)
    except KeyboardInterrupt:  
     gp.cleanup()