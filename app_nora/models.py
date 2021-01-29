from django.db import models
from django.core import validators
import uuid
from django.contrib.auth.models import User


class Usuario(models.Model):

    usuario = models.OneToOneField(User, on_delete = models.CASCADE)

class Menu(models.Model):

    menu_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este menu")

    fecha = models.DateField(auto_now_add=True)
                
    opcion_1 = models.CharField(max_length =60, default=None,
                    validators=[validators.MinLengthValidator(5, "El menu debe contener al menos 5 caracteres"), 
                                validators.MaxLengthValidator(60, "Ingresar dni en el siguiente formato 77111666-5")]
                    )

    opcion_2 = models.CharField(max_length =60, default=None,
                    validators=[validators.MinLengthValidator(5, "El menu debe contener al menos 5 caracteres"), 
                                validators.MaxLengthValidator(60, "El menu debe contener maximo 5 caracteres")]
                    )

    opcion_3 = models.CharField(max_length =60, default=None,
                    validators=[validators.MinLengthValidator(5, "El menu debe contener al menos 5 caracteres"), 
                                validators.MaxLengthValidator(60, "El menu debe contener al menos 5 caracteres")]
                    )

    opcion_4 = models.CharField(max_length =60, default=None,
                    validators=[validators.MinLengthValidator(5, "El menu debe contener al menos 5 caracteres"), 
                                validators.MaxLengthValidator(60, "El menu debe contener al menos 5 caracteres")]
                    )
