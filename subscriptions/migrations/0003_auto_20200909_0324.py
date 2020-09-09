# Generated by Django 3.1.1 on 2020-09-09 03:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_show_subscribers'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscriptions', '0002_subscription_is_subscribed'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together={('user', 'show')},
        ),
    ]
