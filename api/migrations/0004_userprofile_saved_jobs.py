# Generated by Django 4.1.8 on 2023-07-08 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='saved_jobs',
            field=models.ManyToManyField(blank=True, to='api.job'),
        ),
    ]
