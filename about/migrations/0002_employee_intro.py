# Generated by Django 2.2.7 on 2019-11-24 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='intro',
            field=models.TextField(default='To be added - check back soon!'),
            preserve_default=False,
        ),
    ]
