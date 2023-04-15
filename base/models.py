from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    student = 'SV'
    teacher = 'GV'
    admin = 'AD'
    modelaccess = [(student,'SV'),(teacher,'GV'),(admin,'AD')]
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    access = models.CharField(choices=modelaccess,default=student,max_length=2)
    avatar = models.ImageField(upload_to='avatars',null=True, default="avatar.svg")

    def is_access(self):
        return self.access in {self.student, self.teacher, self.admin}

    def __str__(self):
        return f"{self.username}"

class major(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"
    
class subject(models.Model):
    fkmajor = models.ForeignKey(major,on_delete=models.SET_NULL,null=True)
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    subjectcode = models.CharField(primary_key=True,max_length=10)
    name = models.CharField(max_length=200)
    
    modelaccess = (('0','Cơ bản'),('1','Cơ sở'),('2','Chuyên ngành'))
    access = models.CharField(choices=modelaccess,default='0',max_length=2)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
        User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

class chapter(models.Model):
    fksubject = models.ForeignKey(subject,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

class file(models.Model):
    fkchapter = models.ForeignKey(chapter,on_delete=models.SET_NULL,null=True)
    file = models.FileField(upload_to='files',null=True,default=None,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-updated', '-created']

    
class video(models.Model):
    fkchapter = models.ForeignKey(chapter,on_delete=models.SET_NULL,null=True)
    video = models.FileField(upload_to='videos',null=True,default=None,blank=True)
    url = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-updated', '-created']





