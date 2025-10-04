from django.db import models
class UpcommingEvents(models.Model):
    Event_name = models.CharField(max_length=100, default='Event Name')
    Event_desc = models.CharField(default='Event Description')
    Event_img = models.ImageField(upload_to='UpcommingEvents/images', blank=True, null=True)
    Event_title=models.CharField(max_length=100, default='Event Title')
# Create your models here.
