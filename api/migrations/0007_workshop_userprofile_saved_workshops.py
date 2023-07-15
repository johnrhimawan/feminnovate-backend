# Generated by Django 4.1.8 on 2023-07-15 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_userprofile_saved_experiences'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ceated_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=155)),
                ('description', models.TextField(blank=True)),
                ('start_time', models.DateField(blank=True)),
                ('end_time', models.DateField(blank=True)),
                ('location', models.CharField(blank=True, max_length=155)),
                ('website', models.URLField(blank=True, max_length=155)),
                ('picture', models.URLField(blank=True, max_length=155)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='userprofile',
            name='saved_workshops',
            field=models.ManyToManyField(blank=True, to='api.workshop'),
        ),
    ]
