from django.db import models


# Create your models here.
class Fakultas(models.Model):
    nama_fakultas = models.CharField(max_length=150, null=True)
    prodi = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.nama_fakultas

    class Meta:
        db_table = "fakultas"
