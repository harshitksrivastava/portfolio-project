from django.db import models

# Create your models here.

class Technology(models.Model):
    technology_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.technology_name


class Project(models.Model):
    project_image= models.ImageField(upload_to='images/')
    project_title = models.CharField(max_length=20)
    project_summary= models.CharField(max_length=200)
    project_tech = models.ManyToManyField(Technology,default=None)

    def __str__(self):
        return self.project_title
