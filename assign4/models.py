from django.db import models
from django.contrib.auth import get_user_model
from os.path import splitext

class Resume(models.Model):
    docfile = models.FileField(upload_to='temp')

class CV(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    docfile = models.FileField(upload_to='documents/cv/%Y/%m/%d')