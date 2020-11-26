from django.db import models # Del directorio 'django', el subdirectorio 'db', el archivo 'models'
from django.utils import timezone 


class Post(models.Model): # Objeto y sus Atributos o Propiedades.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200) # Argumento 'keyword : value' le indicamos la cantidad.
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now) # Por defecto(default) = Zona horaria(timezone) de ahora(now)
    published_date = models.DateTimeField(
            blank=True, null=True) # Campo en blanco(Blank), Campo nulo(null)

    def publish(self): # Método 'publicar' con sus acciones.
        self.published_date = timezone.now() # Aplica el horario de zona actual
        self.save() # Y lo guarda.

    def __str__(self): # Método
        return self.title  # Devuelve el título ingresado.