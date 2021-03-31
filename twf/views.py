from django.shortcuts import render,redirect
import pyrebase
from django.contrib.auth import logout

config={'apiKey': "AIzaSyC1WhedNrpGOdu4gLYZsfMIOwKMSxEZQ6E",
    'authDomain': "twftask-ba48b.firebaseapp.com",
    'projectId': "twftask-ba48b",
    'databaseURL': "https://twftask-ba48b-default-rtdb.firebaseio.com/",
    'storageBucket': "twftask-ba48b.appspot.com",
    'messagingSenderId': "490451741341",
    'appId': "1:490451741341:web:5b98057c45aeaa72cec274",
    'measurementId': "G-QVHC70X2HL"

}

firebase=pyrebase.initialize_app(config)

authe=firebase.auth()
databasee=firebase.database()

def homepage(request):
    return render(request,'home.html')

def signup_page(request):
    return render(request,'signup.html')

def details_page(request):
    return render(request,'details.html')

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
        uid=user['localId']
        data={"emailid":email}
        databasee.child("users").child(uid).child("email-id").set(data,user['idToken'])
        
        return redirect('details')
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
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    if databasee.child("users").child(user['localId']).child("details").shallow().get().val():
        return render(request,'postlogin.html',{"e":email})
    else:
        return redirect('details')
    

def signout(request):
    try:
        del request.session['uid']
    except KeyError:
        pass
    return redirect('home')

def post_details(request):
    name=request.POST.get('username')
    dob=request.POST.get('dob')
    ffc=request.POST.get('ffc')
    ffp=request.POST.get('ffp')
    try:
        idtoken=request.session['uid']
        user=authe.get_account_info(idtoken)
        user=user['users']
        user=user[0]
        user=user['localId']
        data={"name":name,"Date of Birth":dob,"Favourite football club":ffc,"Favourite football player":ffp}
        databasee.child("users").child(user).child("details").set(data,idtoken)
        return render(request,'postlogin.html')
    except KeyError:
        popup="Oops! User logged out. Please log in again!"
        return render(request,'signin.html',{"popup":popup})
