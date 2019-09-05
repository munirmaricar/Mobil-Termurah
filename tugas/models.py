from django.db import models

# Create your models here.

class Porto(models.Model):
    judulproyek = models.CharField(max_length = 100)
    tanggalmulai = models.DateField()
    tanggalselesai = models.DateField()
    deskripsi = models.TextField()
    tempat = models.CharField(max_length = 100)
    kategori = models.CharField(max_length = 20)