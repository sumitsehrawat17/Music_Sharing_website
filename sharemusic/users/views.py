from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,RegisterForm
from music.models import PublicPrivate,Protected,EmailAllowed
from django.db.models import Q
# Create your views here.

def Home(request):
    if request.user.is_authenticated:
        yours_public_private = PublicPrivate.objects.filter(user=request.user)
        yours_protected = Protected.objects.filter(user=request.user)

        #music share by others as public
        others_public = PublicPrivate.objects.filter(~Q(user = request.user),type_of="public")
        #music share by others as protected
        others_protected = Protected.objects.filter(allowed_emails__in = [request.user.email])
        data = {
            'yours_public_private' : yours_public_private,
            'yours_protected'  : yours_protected,
            'others_public'  : others_public,
            'others_protected' : others_protected
        }
        return render(request,"home.html",context=data)

        

        
    return render(request,"home.html")

def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email = email, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                msg = "Wrong Credentials!!"
                return  render(request,'login.html',context={"msg" : msg})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def LogoutView(request):
    logout(request)
    return redirect('home')
