from django.db import models
from datetime import datetime

class Auto_Camera(models.Model):
    Timers = models.IntegerField(default=0)
    Counters = models.IntegerField(default=0)
    start_Time = models.TimeField()
    stat_Date = models.DateField(default=datetime.now)

    def set_default_start_Time(self):
        return datetime.now().time().replace(second=0)

    def __str__(self):
        template = '{0.Timers} {0.Counters} {0.start_Time}'
        return template.format(self)

    class Meta:
        verbose_name_plural = 'Auto Cameras'


Auto_Camera.start_Time.default = Auto_Camera().set_default_start_Time