# Generated by Django 4.2.2 on 2023-09-22 04:26

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
                ('numerodecohorte', models.IntegerField()),
                ('estadodelacorhorte', models.BooleanField(default=False)),
                ('numerodeparticipantes', models.AutoField(editable=False, primary_key=True, serialize=False)),
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
                ('dni', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999999999)])),
                ('contraseña', models.CharField(max_length=128)),
                ('empleabilidad', models.BooleanField(default=False)),
                ('cohorte', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Dashboard.cohorte')),
                ('empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Dashboard.empresa')),
            ],
        ),
    ]
