# Generated by Django 4.2.5 on 2023-09-21 14:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2023, 9, 21, 14, 41, 19, 814195, tzinfo=datetime.timezone.utc)),
        ),
    ]