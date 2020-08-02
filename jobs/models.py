from django.db import models

# Create your models here.

class Technology(models.Model):
    technology_name = models.CharField(max_length=20)


class Project(models.Model):
    project_image= models.ImageField(upload_to='images/')
    project_title = models.CharField(max_length=20)
    project_summary= models.CharField(max_length=200)
    project_tech = models.ManyToManyField(Technology)
