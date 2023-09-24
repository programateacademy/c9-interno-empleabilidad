# Generated by Django 4.2.2 on 2023-09-24 21:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cohorte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numerodecohorte', models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(999)])),
                ('estadodelacorhorte', models.CharField(choices=[('Activa', 'Activa'), ('No Activa', 'No Activa')], default='Activa', max_length=15)),
                ('numerodeestudiantes', models.PositiveIntegerField(default=0, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('dni', models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(999999999999)])),
                ('contraseña', models.CharField(max_length=128)),
                ('empleabilidad', models.CharField(choices=[('Empleado', 'Empleado'), ('En Proceso', 'En Proceso'), ('Desenpleado', 'Desempleado')], default='Empleado', max_length=15)),
                ('cohorte', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Dashboard.cohorte')),
                ('empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Dashboard.empresa')),
            ],
        ),
    ]
