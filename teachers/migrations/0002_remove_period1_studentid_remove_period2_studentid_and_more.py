# Generated by Django 4.0 on 2022-03-27 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='period1',
            name='studentID',
        ),
        migrations.RemoveField(
            model_name='period2',
            name='studentID',
        ),
        migrations.RemoveField(
            model_name='period3',
            name='studentID',
        ),
        migrations.RemoveField(
            model_name='period4',
            name='studentID',
        ),
    ]
