# Generated by Django 2.0.2 on 2018-08-06 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['order', 'title'], 'verbose_name': 'página', 'verbose_name_plural': 'páginas'},
        ),
        migrations.AddField(
            model_name='page',
            name='order',
            field=models.SmallIntegerField(default=0, verbose_name='Orden'),
        ),
    ]
