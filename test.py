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

Relay = 12
led1=32
led2 = 36
gp.setup(8,gp.IN)  
gp.setup(12,gp.OUT, initial=gp.LOW)  
gp.setup(26,gp.OUT,initial=gp.LOW)  
gp.setup(32,gp.OUT,initial=gp.LOW)
gp.setup(36,gp.OUT,initial=gp.LOW)

firebase = pyrebase.initialize_app(config)
db = firebase.database()

dl=db.child("data").get().val()
dlled = db.child("data_led").get().val()

while True:  
   try:
       
     print(gp.input(8))
     if(gp.input(8) != dl):
         dl = gp.input(8)
         data = {"data":dl}
         db.child("").child().update(data)
     if(dlled != True):
         dlled = True
         data = {"data_led2": dlled}
         db.child("").child().update(data)
     print(32,gp.input(8))
     print(36,gp.input(8))
     gp.output(32,gp.input(8))  
     gp.output(36,not gp.input(8))  
     gp.output(12,gp.input(8))
   except KeyboardInterrupt:  
     gp.cleanup()
