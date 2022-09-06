from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userfolders')
    folder = models.ForeignKey("self", on_delete=models.CASCADE,related_name='folders', null=True, blank=True)
    name = models.CharField(_('Folder Name'), max_length=70)

    def __str__(self):
        return str(self.name)
class File(models.Model):
    name = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userfiles')
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='folderfiles')
    description = models.CharField(max_length=70)
    location = models.FileField( upload_to='uploads/', null=True, blank=True)
    
    def __str__(self):
        return str(self.folder)
    