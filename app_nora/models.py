from django.db import models
from django.core import validators


class Menu(models.Model):

    fecha = models.DateField(max_length=11,
                    validators=[validators.MinLengthValidator(11,"Ingresar Fecha en formato AAAA-MM-DD"),
                                validators.MaxLengthValidator(60, "Ingresar dni en el siguiente formato 77111666-5")]
                    )
                
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
