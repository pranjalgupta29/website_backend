# Generated by Django 2.2.8 on 2019-12-24 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20191219_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='role',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]