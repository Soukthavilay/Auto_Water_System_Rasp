import pyrebase
import os
firebaseConfig = {
  'apiKey': "AIzaSyDdyyHsdfLljDDqcGmBLhqavO3Hb9ywp-U",
  'authDomain': "pbl5-rasberry.firebaseapp.com",
  'databaseURL': "https://pbl5-rasberry-default-rtdb.firebaseio.com",
  'projectId': "pbl5-rasberry",
  "serviceAccount": "pbl5-rasberry-firebase-adminsdk-hggbu-069540d2d7.json",
  'storageBucket': "pbl5-rasberry.appspot.com",
  'messagingSenderId': "50063191700",
  'appId': "1:50063191700:web:369c8c390d8775e92d4e81"
}
firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()
#img = "test1.jpg"
all_files = storage.list_files()

for file in all_files:
  file.download_to_filename(file.name)