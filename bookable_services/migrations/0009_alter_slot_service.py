# Generated by Django 3.2.23 on 2023-12-15 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookable_services', '0008_alter_slot_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookable_services.service'),
        ),
    ]
