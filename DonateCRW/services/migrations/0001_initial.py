# Generated by Django 2.0.2 on 2018-08-23 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Nombre')),
                ('subtitle', models.CharField(max_length=200, verbose_name='Subtítulo')),
                ('wallet_self', models.CharField(max_length=100, verbose_name='Wallet Usuario')),
                ('wallet_shop', models.CharField(max_length=100, verbose_name='Wallet Tienda')),
                ('crw_donate', models.IntegerField(verbose_name='Crown necesarios')),
                ('wallet_donate', models.CharField(blank=True, max_length=100, null=True, verbose_name='Wallet para Donar')),
                ('amount_donate', models.CharField(blank=True, max_length=12, null=True, verbose_name='Saldo donado')),
                ('content', models.TextField(verbose_name='Descripción')),
                ('image', models.ImageField(upload_to='services', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'proyecto',
                'verbose_name_plural': 'proyectos',
                'ordering': ['-created'],
            },
        ),
    ]
