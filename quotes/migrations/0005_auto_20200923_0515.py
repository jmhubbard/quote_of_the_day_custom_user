# Generated by Django 3.1.1 on 2020-09-23 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0004_remove_quote_episode_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='episode_number',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='season_number',
        ),
    ]
