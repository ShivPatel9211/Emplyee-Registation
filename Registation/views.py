from django.shortcuts import render ,redirect
from .models import Employee
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    if request.method == 'POST':
        data=request.POST
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        obj =Employee.objects.create(First_name=first_name,Last_name=last_name,Email=email)
        if obj:
            return redirect('/')
        else:
            return HttpResponse("<h3>Object is not created </h3>")
    else:
        emp =Employee.objects.all()
        context ={
            'emp':emp
        }



    return render(request,'Home.html',context)
@login_required
def update(request , id):
    emp = Employee.objects.get(id=id)

    if request.method  == 'POST':
        emp.First_name=request.POST['first_name']
        emp.Last_name=request.POST['last_name']
        emp.Email=request.POST['email']
        emp.save()
        return redirect('home')
        
    context={
        'emp':emp
    }
    return render(request,'update.html',context)
    
def update(request , id):
    emp = Employee.objects.get(id=id)

    if request.method  == 'POST':
        emp.First_name=request.POST['first_name']
        emp.Last_name=request.POST['last_name']
        emp.Email=request.POST['email']
        emp.save()
        return redirect('home')
        
    context={
        'emp':emp
    }
    return render(request,'update.html',context)


def delete(request , id):
    emp = Employee.objects.get(id=id)

    if request.method  == 'POST':
       emp.delete()
       return redirect('home')
      
        
    context={
        'emp':emp
    }

    return render(request,'delete.html',context)