# Generated by Django 3.1.1 on 2020-09-15 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_show_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
