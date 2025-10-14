from django.db import models

class Leaderboard(models.Model):
    Name = models.CharField(max_length=100, default='Name')
    Score = models.IntegerField(default=0)
    Rank = models.IntegerField(default=0)
    Profile_img = models.ImageField(upload_to='Leaderboard/images', blank=True, null=True)

    def __str__(self):
        return self.Name

