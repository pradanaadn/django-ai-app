from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Cv(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='static/media/cv_upload')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Section(models.Model):
    nama = models.CharField()
    deskripsi = models.TextField()
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class DetailSection(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    nama = models.CharField()
    deskripsi = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class DetailCv(models.Model):
    cv = models.ForeignKey(Cv, on_delete=models.CASCADE)
    detail_section = models.ForeignKey(DetailSection, on_delete=models.CASCADE)
    konten = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    