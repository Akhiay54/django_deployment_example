from django.shortcuts import render
from app5.models import userpro
from app5.forms import userproform,userproinfo
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request,'app5/home.html')
@login_required
def special(request):

    return HttpResponse("logged in : nice !!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def register(request):
    registered = False

    if request.method == "POST":

        user_form = userproform(data=request.POST)
        profile_form = userproinfo(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pics' in request.FILES:

                profile.profile_pics = request.FILES['profile_pics']
            profile.save()

            registered=True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = userproform()
        profile_form = userproinfo()
    return render(request,'app5/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("ACCount not active")
        else:
            print(" someone tried")
            print("username : {} and password : {}".format(username,password))
            return HttpResponse("INVALID login attempt <h1> <a href={% url 'app5:user_login'  %}> login </h1> ")
    else:

        return render(request,'app5/login.html',{})
