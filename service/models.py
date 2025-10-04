from django.db import models
class Features(models.Model):
    Features_name = models.CharField(max_length=100, default='Feature Name')
    Features_price = models.CharField(max_length=100, default='Free')
    Features_desc = models.TextField(default='No description')
    Features_img = models.ImageField(upload_to='service/images', blank=True, null=True)

    

# Create your models here.
