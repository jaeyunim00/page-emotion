from django.contrib import admin
from .models import YouTubeComment
# Register your models here.
@admin.register(YouTubeComment)
class YouTubeCommentAdmin(admin.ModelAdmin):
  pass
