# Generated by Django 4.1.3 on 2022-12-16 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_category_alisting'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alisting',
            old_name='imageurl',
            new_name='imageUrl',
        ),
    ]
