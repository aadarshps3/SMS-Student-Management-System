from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from SMS_app.forms import UserReg, TeacherForm, StudentForm


# Create your views here.

def Index(request):
    return render(request,'Index.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('adminpage')
        elif user is not None and user.is_teacher:
            login(request, user)
            return redirect('teacherpage')
        elif user is not None and user.is_student:
            login(request,user)
            return redirect('studentpage')
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request,'loginpage.html')


def teacher_reg(request):
    form1 = UserReg()
    form2 = TeacherForm()
    if request.method == 'POST':
        form1 = UserReg(request.POST)
        form2 = TeacherForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_teacher = True
            user.save()
            teacher = form2.save(commit=False)
            teacher.user = user
            teacher.save()
            messages.info(request, 'Succesfully Registered')
            return redirect('loginpage')
    return render(request,'teacher_reg.html',{'form1':form1,'form2':form2})

def student_reg(request):
    form1 = UserReg()
    form2 = StudentForm()
    if request.method == 'POST':
        form1 = UserReg(request.POST)
        form2 = StudentForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_student = True
            user.save()
            student = form2.save(commit=False)
            student.user = user
            student.save()
            messages.info(request, 'Succesfully Registered')
            return redirect('loginpage')
    return render(request,'student_reg.html',{'form1':form1,'form2':form2})

def teacherpage(request):
    return render(request,'teacherpage.html')

def studentpage(request):
    return render(request,'studentpage.html')