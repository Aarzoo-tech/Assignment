from django.shortcuts import render
from django.shortcuts import redirect,render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
import folium
import geocoder
from user_records.models import signupUser
from django.views.decorators.csrf import csrf_protect
@csrf_protect
def landingPage(request):
    return render(request,'landing_page.html')
def signUp(request):
    if request.method=="POST":
        userdata=request.POST
        model_object=signupUser()
        model_object.first_name=userdata['firstname']
        model_object.last_name=userdata['lastname']
        model_object.username=userdata['username']
        model_object.password=userdata['password']
        model_object.date_of_birth=userdata['dob']
        model_object.profile_image=userdata['profile']
        model_object.security_question=userdata['security_question']
        model_object.question_answer=userdata['answer']
        model_object.address=userdata['address']
        model_object.save()
        return redirect('http://localhost:8000/login')
    return render(request,'sign_up.html')
def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('http://localhost:8000/user-list')
        else:
            messages.error(request,"Username and Password may Incorrect")
            return redirect('http://localhost:8000/login')
    return render(request,'login.html')
def List_Of_User(request):
    user_list=signupUser.objects.all()
    return render(request,'dashboard.html', {'user_list':user_list})
def show_records_and_edit(request,id):
    user_info=signupUser.objects.get(pk=id)
    return render(request,'studentApp/UserDashboard.html', {'user_info':user_info})
