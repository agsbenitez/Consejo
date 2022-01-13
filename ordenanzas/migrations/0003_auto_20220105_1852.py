# Generated by Django 3.2 on 2022-01-05 21:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ordenanzas', '0002_auto_20220105_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordenanza',
            name='published_date',
        ),
        migrations.AddField(
            model_name='ordenanza',
            name='concejal',
            field=models.CharField(default='', max_length=60, verbose_name='Presentado por'),
        ),
        migrations.AlterField(
            model_name='ordenanza',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de Creación'),
        ),
    ]
