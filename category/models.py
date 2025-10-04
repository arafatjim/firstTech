from django.db import models
class Category(models.Model):
    Category_name =models.CharField(max_length=100, default='Category Name')
    Category_desc =models.TextField(default='No description')
    Category_img =models.ImageField(upload_to='category/images', blank=True, null=True)
# Create your models here.
