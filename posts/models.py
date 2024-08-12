from django.db import models
from datetime import datetime 
import os


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_At = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(null=True, upload_to= 'images/')
    file = models.FileField(null=True, upload_to='files/')
    url = models.URLField(null=True)

    @property
    def file_name(self):
        return os.path.basename(self.file.url) if self.file else ''