# Generated by Django 3.1.1 on 2020-09-14 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_subscription_subscription_preference'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='status',
            field=models.IntegerField(choices=[(None, '(Unknown)'), (0, 'Unknown'), (1, 'Subscribed'), (2, 'Unsubscribed')], default=1),
        ),
    ]
