# Generated by Django 4.2.5 on 2023-10-02 17:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='MobiMarket/media/avatar_images'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2023, 10, 2, 17, 49, 23, 609093, tzinfo=datetime.timezone.utc)),
        ),
    ]