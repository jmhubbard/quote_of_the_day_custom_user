# Generated by Django 3.1.1 on 2020-09-08 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='name',
            field=models.CharField(default='none', max_length=255),
            preserve_default=False,
        ),
    ]
