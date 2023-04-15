from django.contrib import admin
from .models import User,major,subject,chapter,file,video
# Register your models here.

admin.site.register(User)
admin.site.register(major)
admin.site.register(subject)
admin.site.register(chapter)
admin.site.register(file)
admin.site.register(video)
