# Generated by Django 3.1.1 on 2020-09-08 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='is_subscribed',
            field=models.BooleanField(default=True),
        ),
    ]
