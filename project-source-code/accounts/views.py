
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login , logout
from . forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from accounts.models import Donate_Food
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #user = form.save(instance=request.user)
            username = form.cleaned_data['username']
            request.session['username'] = username
            user = form.save()
            login(request , user)
            #username = form.cleaned_data.get('username')
            #messages.success(request , f'Account created for {username} !! ')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request , 'accounts/register.html' , {'form':form})

@login_required
def profile(request):
    return render(request , 'accounts/profile.html')

@csrf_exempt
def Agent_login(request):
	if request.method=="POST":
		na=request.POST.get('Aname')
		pas=request.POST.get('Apassword')
		if na=="Rajit" and pas=="1234":
			return render(request , 'accounts/Agent_login.html' , {})
		else:
			return HttpResponse("Sorry !!!")


@login_required
@csrf_exempt
def Donate(request):
    return render(request , 'accounts/Donate.html' , {})


@login_required
@csrf_exempt
def  Donate_food(request):
	if request.method=="POST":
		ph=request.POST.get('number')
		f=request.POST.get('food')
		a=request.POST.get('address')
		sv = Donate_Food(user=request.user , phone=ph , amount=f , Address=a)
		user = sv.save()
		return HttpResponse('<center><h1>Saved Data</h1></center>')


def status(request):
    details = Donate_Food.objects.filter(user=request.user)
    return render(request , 'accounts/status.html' , {'details' : details})



def Agent_status(request):
    details = Donate_Food.objects.all()
    return render(request , 'accounts/Agent_status.html' , {'details' : details})


def feedback(request):
    return render(request , 'accounts/feedback.html')

@csrf_exempt
def  Feedback(request):
	if request.method=="POST":
		fb=request.POST.get('feedback')
		sv = Donate_Food(user=request.user , FeedBack=fb)
		sv.save()
		return HttpResponse('<center><h1>Send Feedback</h1></center>')
