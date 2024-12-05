from django.db import models

class Proyect(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    estado_alumno = models.CharField(max_length=50, default="Inactivo")
    technology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title   
