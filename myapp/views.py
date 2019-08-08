from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Member
# Create your views here.
def main(request):

    members=Member.objects

    return render(request, 'main.html',{'members' : members})

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            errormsg='잘못 입력하셨습니다.'
            return render(request, 'main.html', {'errormsg' : errormsg})
    else:
        return render(request, 'main.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('main')
    return redirect('main')

def create(request):
    return render(request, 'create.html')

def createmember(request):
    member=Member()
    member.member_name=request.POST['name']
    member.member_code=request.POST['code']
    member.attend=False
    member.save()
    return redirect('main')

def delete(request, member_id):
    member = Member.objects.get(id=member_id)
    member.delete()
    return redirect('main')

def changework(request, member_id):
    if request.method == 'POST':
        member = Member.objects.get(id=member_id)
        code = member.member_code
        confirmcode = request.POST['confirmcode']
        if confirmcode == code:
           
            if member.attend==False:
                member.attend=True
                member.save()
                return redirect('main')

            else:
                member.attend=False
                member.save()
                return redirect('main')
        else:
            errormsg = "개인코드를 잘못 입력하셨습니다."
            return render(request, 'codeconfirm.html', {'member':member ,'errormsg':errormsg})
def codeconfirm(request, member_id):
    member = Member.objects.get(id=member_id)
    return render(request, 'codeconfirm.html', {'member':member})