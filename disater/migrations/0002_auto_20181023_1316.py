# Generated by Django 2.1.2 on 2018-10-23 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disater', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profile_picture',
            field=models.CharField(max_length=50),
        ),
    ]
