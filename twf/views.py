from django.shortcuts import render,redirect
import pyrebase
from django.contrib.auth import logout

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

authe=firebase.auth()

def homepage(request):
    return render(request,'home.html')

def signup_page(request):
    return render(request,'signup.html')

def postsignup_page(request):
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    cpassw=request.POST.get('confpass')
    if passw==cpassw:
        try:
            user=authe.create_user_with_email_and_password(email,passw)
        except:
            popup="User already exists!"
            return render(request,'signup.html',{"popup":popup})
        return render(request,'details.html')
    else:
        popup="Passwords do not match!"
        return render(request,'signup.html',{"popup":popup})

def signin(request):
    return render(request,'signin.html')

def postlogin(request):
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    try:
        user=authe.sign_in_with_email_and_password(email,passw)
    except:
        popup="Invalid Credentials!"
        return render(request,'signin.html',{"popup":popup})
    return render(request,'postlogin.html',{"e":email})

def signout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('home')