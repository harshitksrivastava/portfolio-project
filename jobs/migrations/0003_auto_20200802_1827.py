# Generated by Django 3.0.8 on 2020-08-02 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_project_project_tech'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='technology_name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
