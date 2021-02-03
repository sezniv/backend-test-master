from django.db import models
from django.core import validators
import uuid
from django.contrib.auth.models import User


class Usuario(models.Model):
    
    usuario = models.OneToOneField(User, on_delete = models.CASCADE, default=None)

    rutUsuario = models.CharField(max_length =10, primary_key=True, default=None,
                    validators=[validators.MinLengthValidator(9, "Ingresar dni en el siguiente formato 77111666-5"), 
                                validators.MaxLengthValidator(10, "Ingresar dni en el siguiente formato 77111666-5")]
                    )

class Pedido(models.Model):

    nombre = models.CharField(max_length =100, default=None,
                    validators=[validators.MinLengthValidator(5, "El menu debe contener al menos 5 caracteres"), 
                                validators.MaxLengthValidator(100, "Ingresar dni en el siguiente formato 77111666-5")]
                    )
                    
    list_rol=(('opcion_1','opcion_1'),('opcion_2','opcion_2'),('opcion_3','opcion_3'),('opcion_4','opcion_4'))
    opcion = models.CharField(max_length=15,choices= list_rol,default="Selecciona tu opción")
    comentario = models.CharField(max_length =60, default=None,
                    validators=[validators.MinLengthValidator(2, "Tu comentario no se entiende"), 
                                validators.MaxLengthValidator(60, "Tu comentario puede tener hasta 60 caracteres")]
                    )

class Menu(models.Model):

    menu_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)

    fecha = models.DateField()
                
    opcion_1 = models.CharField(max_length =100, default=None,
                    validators=[validators.MinLengthValidator(5, "El menu debe contener al menos 5 caracteres"), 
                                validators.MaxLengthValidator(100, "Ingresar dni en el siguiente formato 77111666-5")]
                    )

    opcion_2 = models.CharField(max_length =100, default=None,
                    validators=[validators.MinLengthValidator(5, "El menu debe contener al menos 5 caracteres"), 
                                validators.MaxLengthValidator(100, "El menu debe contener maximo 5 caracteres")]
                    )

    opcion_3 = models.CharField(max_length =100, default=None,
                    validators=[validators.MinLengthValidator(5, "El menu debe contener al menos 5 caracteres"), 
                                validators.MaxLengthValidator(100, "El menu debe contener al menos 5 caracteres")]
                    )

    opcion_4 = models.CharField(max_length =100, default=None,
                    validators=[validators.MinLengthValidator(5, "El menu debe contener al menos 5 caracteres"), 
                                validators.MaxLengthValidator(100, "El menu debe contener al menos 5 caracteres")]
                    )
