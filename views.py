from django.shortcuts import render,redirect
from .forms import RegisterForm

# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)
    if request.method =="POST":
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register')
    
    return render(request, template_name='users/register.html', context={'form':form})