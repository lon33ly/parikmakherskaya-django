# Generated by Django 3.1 on 2021-06-06 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0030_auto_20210607_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preorder',
            name='reserved_date',
            field=models.TextField(null=True, verbose_name='Дата брони'),
        ),
    ]
