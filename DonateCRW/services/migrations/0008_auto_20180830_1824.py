# Generated by Django 2.0.2 on 2018-08-30 18:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_service_finish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='finish',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Finish'),
        ),
    ]
