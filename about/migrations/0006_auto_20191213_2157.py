# Generated by Django 2.2.8 on 2019-12-13 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_casestudyimage_alt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='profile_pic',
        ),
        migrations.DeleteModel(
            name='CaseStudyImage',
        ),
    ]
