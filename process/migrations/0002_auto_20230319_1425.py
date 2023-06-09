# Generated by Django 3.2.18 on 2023-03-19 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='groups',
            field=models.ManyToManyField(blank=True, to='auth.Group'),
        ),
        migrations.AddField(
            model_name='process',
            name='permissions',
            field=models.ManyToManyField(blank=True, to='auth.Permission'),
        ),
    ]
