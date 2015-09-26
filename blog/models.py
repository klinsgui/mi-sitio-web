from django.db import models
from django.utils import timezone #Para ver la fecha del sistema

class Postear(models.Model):
    autor = models.ForeignKey('auth.User') #models es la BD, y se importa la llave foranea
    titulo = models.CharField(max_length=200) #campo texto con maximo largo 200
    texto = models.TextField() #para texto, sin limite
    fecha_creacion = models.DateTimeField(
                default=timezone.now)
    fecha_publicacion = models.DateTimeField(
                blank=True, null=True)

    def publicar(self):#Self, todos los datos los recibe él mismo
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
