# Generated by Django 4.0.5 on 2023-03-21 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_alter_bids_options_alter_comments_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlist',
            name='uid',
        ),
    ]
