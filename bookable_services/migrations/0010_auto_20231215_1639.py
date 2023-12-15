# Generated by Django 3.2.23 on 2023-12-15 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookable_services', '0009_alter_slot_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slot',
            name='place',
        ),
        migrations.RemoveField(
            model_name='slot',
            name='service',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='slot',
        ),
        migrations.RemoveField(
            model_name='service',
            name='description_detail_bullets',
        ),
        migrations.RemoveField(
            model_name='service',
            name='description_summary',
        ),
        migrations.RemoveField(
            model_name='service',
            name='regions',
        ),
        migrations.AddField(
            model_name='service',
            name='description',
            field=models.TextField(default='Standard service'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='service_images/'),
        ),
        migrations.AddField(
            model_name='service',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='service_images/'),
        ),
        migrations.AddField(
            model_name='service',
            name='key_features',
            field=models.TextField(default='Clean', help_text='Enter key features separated by commas'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='service',
            field=models.ForeignKey(default='Standard', on_delete=django.db.models.deletion.CASCADE, to='bookable_services.service'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.DeleteModel(
            name='Place',
        ),
        migrations.DeleteModel(
            name='Slot',
        ),
    ]
