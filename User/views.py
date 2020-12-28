from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm ,User
from django.contrib.auth import authenticate,login , logout

# Create your views here.
def register(request):
    if request.method== 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=User.objects.create(username=data['username'])
            user.set_password(data['password1'])
            user.save()
            return redirect('home')

    form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request,'register.html' , context)

def Userlogin(request):
    if request.method == 'POST':
        data=request.POST
        user = authenticate(request,username=data['username'],password = data['password'])
        print(user)
        if user is not None:
            login(request,user)
            return redirect('home')

    return render(request, 'login.html')

def Userlogout(request):
    logout(request)
    return redirect('/login')
    