from django.http import HttpResponse
from .forms import MyUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User,subject,major,chapter,file,video
from .forms import MyUserCreationForm, UserForm, SubjectForm, ChapterForm,fileForm,videoForm
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    subjects = subject.objects.filter(
        Q(fkmajor__name__icontains=q) |
        Q(name__icontains=q)
    )
    # users = User.objects.filter(
    #     Q(name__icontains=q)
    # )
    users = User.objects.all()
    majors = major.objects.all()
    
    subject_count = subjects.count()
    context = {'subjects': subjects,'subject_count':subject_count,
                'majors': majors,'users': users}

    return render(request,'base/home.html',context)

def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Người dùng không tồn tại')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Tài khoản hoặc mật khẩu không chính xác!!')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/login_register.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('home')



@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'base/update_user.html', {'form': form})

@login_required(login_url='login')
def createSubject(request):
    form = SubjectForm()
    majors = major.objects.all()
    sbj = subject.objects.all()
    if request.method == 'POST':
        major_name = request.POST.get('major')
        majorss, created = major.objects.get_or_create(name=major_name)
        subject.objects.create(
            host=request.user,
            fkmajor=majorss,
            name=request.POST.get('name'),
            subjectcode=request.POST.get('subjectcode'),
            access=request.POST.get('access'),
        )
        return redirect('home')

    context = {'form': form, 'majors':majors,'sbj':sbj}
    return render(request, 'base/subject_form.html', context)



@login_required(login_url='login')
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    majors = major.objects.all()
    subjects = user.subject_set.all()
    context = {'user': user,'majors':majors,'subjects':subjects}
    return render(request, 'base/profile.html', context)


def Subject(request, pk):
    subjects = subject.objects.get(subjectcode=pk)
    chapters = chapter.objects.all()
    participants = subjects.participants.all()
    context = {'subjects': subjects,
               'participants': participants,
               'chapters':chapters,
               }
    return render(request, 'base/subject.html', context)

@login_required(login_url='login')
def createChapter(request,pk):
    form = ChapterForm()
    subjects = subject.objects.get(subjectcode=pk)
    chapters = chapter.objects.all()
    if request.method == 'POST':
        chapter.objects.create(
            fksubject= subjects,
            name=request.POST.get('name'),
        )
        return redirect('subject', pk=pk)
    context = {'form': form,'subjects': subjects,'chapters':chapters}
    return render(request, 'base/chapter_form.html', context)

@login_required(login_url='login')
def deleteSubject(request,pk):
    subjects = subject.objects.get(subjectcode=pk)
    if request.method == 'POST':
        subjects.delete()
        return redirect('home')
    return render(request, 'base/delete_subject.html',{'subjects': subjects})

def Chapter(request,pk):
    form =  fileForm()
    chapters = chapter.objects.get(id = pk)
    files = file.objects.all()
    if request.method == 'POST':
        file.objects.update_or_create(
            fkchapter= chapters,
            file= request.FILES['file']
        )
        return redirect('chapter', pk=pk)
    else:
        form = fileForm()
    context = {'form': form, 'chapters': chapters, 'files': files}
    return render(request, 'base/chapter.html',context)

def Major(request,pk):
    majorss = major.objects.get(id = pk)
    subjects = subject.objects.all()
    context = {'majorss':majorss, 'subjects':subjects}
    return render(request, 'base/major.html',context)

def Teacher(request):
    Users = User.objects.all()
    context = {'Users':Users}
    return render(request, 'base/teacher.html',context)