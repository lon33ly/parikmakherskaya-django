# Generated by Django 3.2.2 on 2021-05-24 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0024_auto_20210520_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.date'),
        ),
    ]
