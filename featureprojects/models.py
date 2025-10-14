from django.db import models
class FeatureProjects(models.Model):
    Project_name = models.CharField(max_length=100, default ='Project Name')
    Project_manager =models.CharField(max_length=100, default ='Project Manager')
    Project_desc = models.CharField(default='Project Description', max_length=300)
# Create your models here.
