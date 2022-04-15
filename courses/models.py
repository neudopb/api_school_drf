from django.db import models


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
        ordering = ["id"]

    def __str__(self):
        return self.title

    
class Evaluation(Base):
    course = models.ForeignKey(
        Course, related_name="evaluations", 
        on_delete=models.CASCADE, verbose_name="Curso"
    )
    name = models.CharField(max_length=255, verbose_name="Nome")
    email = models.EmailField(verbose_name="E-mail")
    comment = models.TextField(blank=True, default="", verbose_name="Comentário")
    note = models.DecimalField(max_digits=2, decimal_places=1, verbose_name="Nota")

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        unique_together = ["course", "email"]
        ordering = ["id"]

    def __str__(self):
        return f"{self.course} - {self.name}"