# Generated by Django 3.1.1 on 2020-09-24 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0009_quote_speaker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='speaker_name',
        ),
    ]
