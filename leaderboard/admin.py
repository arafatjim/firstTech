from django.contrib import admin
from leaderboard.models import Leaderboard
from leaderboard.models import Leaderboard
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Score', 'Rank', 'Profile_img')
admin.site.register(Leaderboard)

# Register your models here.
