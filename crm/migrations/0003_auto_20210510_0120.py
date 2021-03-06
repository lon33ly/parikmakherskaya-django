# Generated by Django 3.2.1 on 2021-05-09 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20210509_2358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('finish_time', 'total_price'), 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterField(
            model_name='order',
            name='master_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.master', verbose_name='Мастер'),
        ),
        migrations.AlterField(
            model_name='preorder',
            name='reserved_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.timetable', verbose_name='Дата брони'),
        ),
    ]
