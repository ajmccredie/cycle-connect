# Generated by Django 3.2.23 on 2023-12-16 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookable_services', '0015_auto_20231216_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description_detail_bullets',
            field=models.TextField(help_text="Enter key features separated by '~'"),
        ),
    ]