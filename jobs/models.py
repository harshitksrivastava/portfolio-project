from django.db import models

# Create your models here.

class Project(models.Model):
    project_image= models.ImageField(upload_to='images/')
    project_title = models.CharField(max_length=20)
    proejct_summary= models.CharField(max_length=200)
