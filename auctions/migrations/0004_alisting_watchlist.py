# Generated by Django 4.1.3 on 2022-12-17 12:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_rename_imageurl_alisting_imageurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='alisting',
            name='WatchList',
            field=models.ManyToManyField(blank=True, null=True, related_name='WatchList', to=settings.AUTH_USER_MODEL),
        ),
    ]
