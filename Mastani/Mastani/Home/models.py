from django.db import models

# Create your models here.

class literasi (models.Model):
    title = models.CharField(max_length=256)
    deskripsi = models.TextField(max_length=2000)
    author = models.CharField(max_length=100)
    created_date = models.DateField()
    link_literasi = models.CharField(max_length=256, default='default_link')
    img = models.ImageField(upload_to='img_literasi', null=True, blank=True)

    def __str__(self):
        return self.title