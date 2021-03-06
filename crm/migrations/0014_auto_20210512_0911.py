# Generated by Django 3.2.2 on 2021-05-12 06:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0013_service_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='photo',
            field=models.FileField(upload_to='masters_photo/', validators=[django.core.validators.FileExtensionValidator(['svg', 'png', 'jpeg'])], verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='service',
            name='photo',
            field=models.FileField(upload_to='services_photo/', validators=[django.core.validators.FileExtensionValidator(['svg', 'png', 'jpeg'])], verbose_name='Фото'),
        ),
    ]
