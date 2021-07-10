# Generated by Django 3.2.1 on 2021-05-10 22:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0010_auto_20210511_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='photo',
            field=models.FileField(upload_to='masters_photo/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpeg', 'svg'])], verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='service',
            name='photo',
            field=models.FileField(upload_to='services_photo/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpeg', 'svg'])], verbose_name='Фото'),
        ),
    ]
