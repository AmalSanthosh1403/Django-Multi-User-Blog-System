from django.shortcuts import render,redirect
from . models import *
from django.http import HttpResponse,HttpResponseRedirect

def login(request):
    if request.method=="POST":
        email1=request.POST.get('email')
        pass1=request.POST.get('password')
        objs=usertbl.objects.filter(useremail=email1,userpassword=pass1)

        if objs:
            for obj in objs:
                request.session['user_id']=obj.id
            return redirect('/home')
        else:
            return render(request,'login.html',{'errormsg_login':'Invalid Username or Password'})
    return render(request,'login.html')

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        return redirect('/')

def reg(request):
    if request.method=='POST':
        name1=request.POST.get('name')
        age1=request.POST.get('age')
        phone1=request.POST.get('phone')
        email1=request.POST.get('email')
        pass1=request.POST.get('password')
        
        already_exits=usertbl.objects.filter(useremail=email1)
        if already_exits:
            return render(request,'reg.html',{'errorMsg_reg':'Email already exists'})
        else:
            newobj=usertbl.objects.create(
                username=name1,
                userage=age1,
                userphone=phone1,
                useremail=email1,
                userpassword=pass1
            )
            newobj.save()
            return render(request,'login.html')
    return render(request,'reg.html')

def home(request):
    postobjs=posttbl.objects.all()
    currentuserobj=usertbl.objects.get(id=request.session['user_id'])
    return render(request,'home.html',{'postobjs':postobjs,'loggedusername':currentuserobj.username,'loggeduserobj':currentuserobj})

def profile(request):
    obj=usertbl.objects.get(id=request.session['user_id'])
    return render(request,'myprofile.html',{"userid":obj})

def adminapproval(request):
    obj=usertbl.objects.get(id=request.session['user_id'])
    return render(request,'adminapproval.html',{"userid":obj})

def createpost(request):
    if request.method=='POST':
        tl=request.POST.get('tl')
        cn=request.POST.get('cn')
        post_obj=posttbl.objects.create(
            title=tl,
            content=cn,
            userid=usertbl.objects.get(id=request.session['user_id'])
        )
        post_obj.save()

        return redirect('/home')
    else:
        return render(request,'createpost.html')
    
def detailview(request):
    temp=request.GET.get('idn')
    post_objs=posttbl.objects.get(id=temp)
    request.session['post_id']=temp
    comment_objs=commenttbl.objects.filter(postidPF=post_objs.id).order_by('-created_updated_at')
    currentuserobj=usertbl.objects.get(id=request.session['user_id'])
    return render(request,'detailview.html',{'post_obj':post_objs,'comment_obj':comment_objs,'loggeduserobj':currentuserobj})

def myblog(request):
    my_objs=posttbl.objects.filter(userid=request.session['user_id'])
    loggeduserobj=usertbl.objects.get(id=request.session['user_id'])
    return render(request,'myblogs.html',{'my_obj':my_objs,'loggeduserobj':loggeduserobj})

def editmypost(request,postidv):
    edit_obj=posttbl.objects.get(id=postidv)
    if request.method=="POST":
        tl=request.POST.get('tl')
        cn=request.POST.get('cn')
        edit_obj.title=tl
        edit_obj.content=cn
        edit_obj.save()
        return redirect('/myblog')
    return render(request,'editmyblog.html',{'editobj':edit_obj})

def deletemypost(request,postidv):
    delete_obj=posttbl.objects.get(id=postidv)
    delete_obj.delete()
    return redirect('/myblog')

def search(request):
    if request.method=='POST':
        searchvalue=request.POST.get('searchvalue')
        obj=posttbl.objects.filter(title__icontains=searchvalue)
        return render(request,'search.html',{'objs':obj})
    return redirect('/home')

def addcomment(request):
    if request.method=='POST':
        cnt=request.POST.get('cnt')
        comment_obj=commenttbl.objects.create(
            commentcontent=cnt,
            postidPF=posttbl.objects.get(id=request.session['post_id']),
            useridUF=usertbl.objects.get(id=request.session['user_id'])
        )
        comment_obj.save()
        temp=request.session["post_id"]
        return redirect(f'/detailview?idn={temp}')
    
def like(request):
    current_userid=request.session['user_id']
    current_userobj=usertbl.objects.get(id=current_userid)
    current_postid=request.GET.get('idn')
    current_postobj=posttbl.objects.get(id=current_postid)
    if  current_postobj.likeddetails.filter(id=current_userobj.id).exists():
        current_postobj.likeddetails.remove(current_userobj)
        current_postobj.likes-=1
    else:
        current_postobj.likeddetails.add(current_userobj)
        current_postobj.likes+=1
    current_postobj.save()
    return redirect('/home')
    # hi hello