# Generated by Django 3.2.23 on 2023-12-20 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookable_services', '0016_alter_service_description_detail_bullets'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='service_images/'),
        ),
    ]
