from django.db import models

# Create your models here.


class Project(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.title
