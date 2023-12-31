# Generated by Django 3.2.23 on 2023-12-15 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookable_services', '0005_booking_individual_slot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slot',
            old_name='max_people',
            new_name='max_participants',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='individual_slot',
        ),
        migrations.AddField(
            model_name='slot',
            name='current_participants',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='slot',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookable_services.service'),
        ),
        migrations.DeleteModel(
            name='IndividualSlot',
        ),
    ]
