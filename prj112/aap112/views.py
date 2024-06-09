from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, logout,authenticate
from .models import Task
from .forms import Todo_form


def home1(request):
    return render(request,'home1.html')



def Index(request):
     task = Task.objects.all()
     return render(request,'index.html',{"task":task})



def todo_create(request):
    if request.method == 'POST':
         tdform = Todo_form(request.POST)
         if tdform.is_valid():
             tdform.save()
             return redirect('Index')
    else:
        tdform = Todo_form()
        return render(request,'createform.html',{"tdform":tdform})
    


def todo_update(request,id):
    todo = get_object_or_404(Task,id=id)
    if request.method == 'POST':
         tdform= Todo_form(request.POST,instance=todo)
         if tdform.is_valid():
             tdform.save()
             return redirect('Index')
    else:
        tdform=Todo_form()
    return render(request,'createform.html',{"tdform":tdform})
    



def todo_delete(request,id):
    todo=get_object_or_404(Task,id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('Index')
    else:
        tdform=Todo_form()
        return render(request,'index.html',{"tdform":tdform})




def signup1(request):
    if request.method == 'POST':
        forms = UserCreationForm(request.POST)
        if forms.is_valid():
            forms.save()
            username = forms.cleaned_data.get("username")
            password = forms.cleaned_data.get("password1")
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('login1')
    else:
        forms = UserCreationForm()
    return render(request,'signup1.html',{"forms":forms})



def login_view(request):
    if request.method == 'POST':
        forms = AuthenticationForm(request, data=request.POST)
        if forms.is_valid():
            username= forms.cleaned_data.get("username")
            password= forms.cleaned_data.get("password")
            user= authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('Index')
            
    else:
        forms= AuthenticationForm()
    return render(request,'login1.html',{"forms":forms})



def logout_view(request):
    logout(request)
    return redirect('home1')


