# Generated by Django 3.1.2 on 2020-10-28 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Body',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='Title',
            new_name='title',
        ),
    ]
