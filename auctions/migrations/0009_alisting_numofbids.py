# Generated by Django 4.1.3 on 2022-12-26 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_bid_alter_alisting_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='alisting',
            name='NumOfBids',
            field=models.IntegerField(default=0),
        ),
    ]
