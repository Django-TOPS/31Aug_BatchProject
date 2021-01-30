from django.shortcuts import render,HttpResponse,redirect
from .forms import NewUserForm, NotesForm
from .models import NewUser, notes
from django.contrib.auth import logout
from django.core.mail import send_mail
from MySiteProject import settings
from twilio.rest import Client
from django.contrib.auth.decorators import login_required
import random

# Create your views here.

def login(request):
  return render(request, 'login.html')

@login_required
def home(request):
  return render(request, 'home.html')

  
def index(request):
    if request.method=='POST':
        myfrm=NewUserForm(request.POST)
        if request.POST.get('login')=='login':
            username=request.POST['username']
            password=request.POST['password']
            
            user_login=NewUser.objects.filter(username=username,password=password)
            if user_login:
                uid=NewUser.objects.get(username=username)
                print("UserID:",uid.id)

                request.session['uid']=uid.id
                request.session['username']=username
                print('Login Successfully!')

                #Message Sending
                #account_sid = os.environ['AC46a17b69017789108be25ce35f098560']
                #auth_token = os.environ['a8ba3c26ec0760289cb06862cf413477']
                client = Client('AC46a17b69017789108be25ce35f098560', 'a8ba3c26ec0760289cb06862cf413477')

                otp=random.randint(11111,99999)
                message = client.messages.create(
                     body=f"Hii... Thanks for register with us! Have a nice day! Your OTP is {otp}",
                     from_='+17144521960',
                     to='+919712039866'
                 )
                print(message.sid)
                return redirect('profile')
            else:
                print('Error...Invalid Username or Password!')
        elif request.POST.get('signup')=='signup':
            if myfrm.is_valid():
                myfrm.save()
                user=NewUser()

                #Sending Confirmation MAIL
                subject = 'Email Confirmation usign Django'
                message = f'Hi {user.username}, thank you for register with us!'
                email_from = settings.EMAIL_HOST_USER 
                recipient_list = ['mayur65parmar@gmail.com','ethan6112000@gmail.com'] 
                send_mail(subject, message, email_from, recipient_list) 
                print('Confirmation main send...!')

                print('New user created....')
                return redirect('profile')
            else:
                print(myfrm.errors)
    else:
        myfrm=NewUserForm()
    return render(request,'index.html',{'myfrm':myfrm})

def profile(request):
    user=request.session.get("username")
    
    if request.method=='POST':
        mynote=NotesForm(request.POST,request.FILES)
        if mynote.is_valid():
            mynote.save()
            print('Your Notes has been uploaded!')
        else:
            print("Error...Plz try again.")
    else:
        mynote=NotesForm()
    return render(request,'profile.html',{'user':user,'mynote':mynote})

def user_logout(request):
    logout(request)
    return redirect('/')

def updateprofile(request):
    userid=request.session.get('uid')
    print("Your UserID:",userid)
    if request.method=='POST':
        myfrm=NewUserForm(request.POST)
        id=NewUser.objects.get(id=userid)
        if myfrm.is_valid():
            myfrm=NewUserForm(request.POST, instance=id)
            myfrm.save()
            return redirect('profile')
        else:
           print("Error...Somthing went wrong.")
    else:
        myfrm=NewUserForm()
    return render(request,'updateprofile.html',{'myfrm':myfrm,'userdata':NewUser.objects.get(id=userid)})


def notfound(request):
    return render(request,'404.html')