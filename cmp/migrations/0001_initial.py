# Generated by Django 4.1 on 2022-09-17 03:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(max_length=100, unique=True, verbose_name='Nombre de proveedor')),
                ('direccion', models.CharField(blank=True, max_length=250, null=True, verbose_name='Direccion')),
                ('contacto', models.CharField(max_length=100, verbose_name='Contacto')),
                ('telefono', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefono')),
                ('email', models.CharField(blank=True, max_length=150, null=True, verbose_name='Email')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
    ]