# Generated by Django 5.0.2 on 2025-03-15 03:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_escolar_api', '0002_administradores_delete_profiles'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('matricula', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_nacimiento', models.DateTimeField(blank=True, null=True)),
                ('curp', models.CharField(blank=True, max_length=255, null=True)),
                ('rfc', models.CharField(blank=True, max_length=255, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('telefono', models.CharField(blank=True, max_length=255, null=True)),
                ('ocupacion', models.CharField(blank=True, max_length=255, null=True)),
                ('creation', models.DateTimeField(auto_now_add=True, null=True)),
                ('update', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Maestros',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('id_maestro', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_nacimiento', models.DateTimeField(blank=True, null=True)),
                ('telefono', models.CharField(blank=True, max_length=255, null=True)),
                ('rfc', models.CharField(blank=True, max_length=255, null=True)),
                ('cubiculo', models.CharField(blank=True, max_length=255, null=True)),
                ('area_investigacion', models.CharField(blank=True, max_length=255, null=True)),
                ('materias_json', models.TextField(blank=True, null=True)),
                ('creation', models.DateTimeField(auto_now_add=True, null=True)),
                ('update', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
