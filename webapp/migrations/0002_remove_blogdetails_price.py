# Generated by Django 3.1.4 on 2021-04-30 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogdetails',
            name='Price',
        ),
    ]
