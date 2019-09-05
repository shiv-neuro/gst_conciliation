from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
import sys
from subprocess import run,PIPE
# Create your views here.
def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        print('ths is a user',user)

        if user is not None:
            auth.login(request, user)
            
            return redirect('data')
        else :
            messages.info(request,'invalid credentials')
            return redirect(login)
    else:
        return render(request,'login.html')

def data_html(request):
    return render(request,'data.html')

def gst_page(request):    
    inp = request.POST.get('param') 
    print(inp) 

    out = run([sys.executable,'C://Users//Shiv//Desktop//django_projects//gst_conciliation//test.py',inp],shell=False,stdout =PIPE)
    print (out)
    return render(request,'data.html',{'data1':out.stdout})