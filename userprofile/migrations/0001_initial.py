# Generated by Django 3.2.23 on 2023-11-06 11:22

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biography', models.TextField(blank=True)),
                ('profile_picture', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('cycling_skills', models.CharField(blank=True, max_length=100)),
                ('preferred_ride_type', models.CharField(blank=True, max_length=100)),
                ('maintenance_skills', models.CharField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
