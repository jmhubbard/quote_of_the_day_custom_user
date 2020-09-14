# Generated by Django 3.1.1 on 2020-09-13 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_auto_20200909_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='subscription_preference',
            field=models.CharField(choices=[('Subscribed', 'Subscribed'), ('Unsubscribed', 'Unsubscribed')], default='Subscribed', max_length=20),
        ),
    ]
