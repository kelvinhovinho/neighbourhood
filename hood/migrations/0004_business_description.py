# Generated by Django 2.2.6 on 2019-10-26 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0003_business'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
