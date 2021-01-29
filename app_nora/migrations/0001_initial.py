# Generated by Django 3.1.5 on 2021-01-28 21:07

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_uuid', models.UUIDField(default=uuid.uuid4, help_text='ID único para este menu', primary_key=True, serialize=False)),
                ('fecha', models.DateField(max_length=11, validators=[django.core.validators.MinLengthValidator(11, 'Ingresar Fecha en formato AAAA-MM-DD'), django.core.validators.MaxLengthValidator(60, 'Ingresar dni en el siguiente formato 77111666-5')])),
                ('opcion_1', models.CharField(default=None, max_length=60, validators=[django.core.validators.MinLengthValidator(5, 'El menu debe contener al menos 5 caracteres'), django.core.validators.MaxLengthValidator(60, 'Ingresar dni en el siguiente formato 77111666-5')])),
                ('opcion_2', models.CharField(default=None, max_length=60, validators=[django.core.validators.MinLengthValidator(5, 'El menu debe contener al menos 5 caracteres'), django.core.validators.MaxLengthValidator(60, 'El menu debe contener maximo 5 caracteres')])),
                ('opcion_3', models.CharField(default=None, max_length=60, validators=[django.core.validators.MinLengthValidator(5, 'El menu debe contener al menos 5 caracteres'), django.core.validators.MaxLengthValidator(60, 'El menu debe contener al menos 5 caracteres')])),
                ('opcion_4', models.CharField(default=None, max_length=60, validators=[django.core.validators.MinLengthValidator(5, 'El menu debe contener al menos 5 caracteres'), django.core.validators.MaxLengthValidator(60, 'El menu debe contener al menos 5 caracteres')])),
            ],
        ),
    ]