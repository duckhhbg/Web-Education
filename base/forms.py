from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User,major,subject,chapter,file,video

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email']

class MajorForm(ModelForm):
    class Meta:
        model = major
        fields = ['name']

class SubjectForm(ModelForm):
    class Meta:
        model = subject
        fields = '__all__'
        exclude = ['host','participans']

class ChapterForm(ModelForm):
    class Meta:
        model = chapter
        fields = '__all__'
        exclude = ['fksubject']

class fileForm(ModelForm):
    class Meta:
        model = file
        fields = ['fkchapter','file']
        exclude = ['fkchapter']

class videoForm(ModelForm):
    class Meta:
        model = video
        fields = ['video']
        exclude = ['fkchapter']