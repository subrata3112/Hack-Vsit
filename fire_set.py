'''
<!-- The core Firebase JS SDK is always required and must be listed first -->
<script src="https://www.gstatic.com/firebasejs/7.8.0/firebase-app.js"></script>

<!-- TODO: Add SDKs for Firebase products that you want to use
     https://firebase.google.com/docs/web/setup#available-libraries -->
<script src="https://www.gstatic.com/firebasejs/7.8.0/firebase-analytics.js"></script>

<script>
'''
''' 
var firebaseConfig = {
    "apiKey": "AIzaSyAqGk4Z_2QAE0JSyvVNDkjhRUmrg1apot0",
    "authDomain": "vsit-2be9f.firebaseapp.com",
    "databaseURL": "https://vsit-2be9f.firebaseio.com",
    "projectId": "vsit-2be9f",
    "storageBucket": "vsit-2be9f.appspot.com",
    "messagingSenderId": "443551929217",
    "appId": "1:443551929217:web:83d9e1fe6429f56b5c4e80",
    "measurementId": "G-2M0SJERF9S"
}
  
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  firebase.analytics();
</script>

firbase = pyrebase.initialize_app(Config)
db = firbase.database()
app = Flask(__name__)
db.("place").remove()
name = db.child("place").get()
place = name.val()
places = place.values()
'''
