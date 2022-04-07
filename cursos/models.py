from django.db import models

# Create your models here.

class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Criado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Atualizado")
    is_active = models.BooleanField(default=True, verbose_name="Ativo")

    class Meta:
        abstract = True


class Course(Base):
    title = models.CharField(max_length=255, verbose_name="Título")
    url = models.URLField(unique=True, verbose_name="URL")

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.title