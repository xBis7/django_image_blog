# Generated by Django 3.0.6 on 2020-06-14 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_blog', '0004_auto_20200613_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
    ]
