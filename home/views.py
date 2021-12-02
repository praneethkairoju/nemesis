 
from django.shortcuts import render , redirect
from .forms import SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . models import CustomUser
from django.contrib import messages




# Create your views here.
@login_required(login_url='login')
def index(request):
    data = CustomUser.objects.all()
    
    return render(request, 'index.html', {'name': data})

def signuppage(request):
    if request.method == "POST":   
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {name}')
        return redirect('login')
    else:
        
        form = SignupForm()
    return render(request, 'signup.html', {'form' : form })        

def loginpage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Wellcome {username} ')
            return redirect('index-home')
        else:
            messages.info(request, 'Email or Password is incorrect')
               
  
    return render(request, 'login.html')  

def logoutpage(request):
    logout(request)
    return redirect('login')
