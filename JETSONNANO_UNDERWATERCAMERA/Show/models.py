from django.db import models

# Create your models here.
class Auto_Camera(models.Model):
    Timers = models.IntegerField(default=0)
    Couters = models.IntegerField(default=0)

    def __str__(self):
        template = '{0.Timers} {0.Couters}'
        return template.format(self)