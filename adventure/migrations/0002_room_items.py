# Generated by Django 3.0.2 on 2020-02-01 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='items',
            field=models.CharField(default='DEFAULT TITLE', max_length=100),
        ),
    ]
