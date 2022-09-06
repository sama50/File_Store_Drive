from django.contrib import admin
from app.models import Folder , File
# Register your models here.

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ('id','user','folder','name')

@admin.register(File)
class FolderAdmin(admin.ModelAdmin):
    list_display = ('id','user','folder','description','location')