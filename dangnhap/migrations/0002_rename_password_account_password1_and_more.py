# Generated by Django 4.0.5 on 2022-06-08 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dangnhap', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='password',
            new_name='password1',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='username',
            new_name='username1',
        ),
    ]
