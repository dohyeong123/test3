# Generated by Django 2.2.3 on 2019-08-03 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='attend',
            field=models.BooleanField(default=True),
        ),
    ]
