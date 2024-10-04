from django.shortcuts import render,redirect
from . models import *
from userapp.models import *

# def adminLogin(request):
#     if request.method=='POST':
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         objs=admintbl.objects.filter(adminemail=email,adminpassword=password)
#         if objs:
#             for i in objs:
#                 request.session['admin_user_id']=i.id
#             return redirect('/adminapp/home')
#         else:
#             return render(request,'adminlogin.html',{'errormsg_login':'Invalid Username or Password'})
#     return render(request,'adminlogin.html')



def adminLogout(request):
    if 'admin_user_id' in request.session:
        del request.session['admin_user_id']
        return redirect('/adminapp/login')
    
def adminHome(request):
    return render(request,'adminhome.html')


