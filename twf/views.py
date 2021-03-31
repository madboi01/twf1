from django.shortcuts import render
import pyrebase

config={'apiKey': "AIzaSyC1WhedNrpGOdu4gLYZsfMIOwKMSxEZQ6E",
    'authDomain': "twftask-ba48b.firebaseapp.com",
    'projectId': "twftask-ba48b",
    'databaseURL': "https://databaseName.firebaseio.com",
    'storageBucket': "twftask-ba48b.appspot.com",
    'messagingSenderId': "490451741341",
    'appId': "1:490451741341:web:5b98057c45aeaa72cec274",
    'measurementId': "G-QVHC70X2HL"

}

firebase=pyrebase.initialize_app(config)

auth=firebase.auth()

def signin(request):
    return render(request,'signin.html')

def postsign(request):
    return render(request,'home.html')