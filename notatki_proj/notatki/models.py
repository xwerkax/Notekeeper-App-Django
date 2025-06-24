from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Notatka(models.Model):
    tytul = models.CharField(max_length=200)
    przedmiot = models.CharField(max_length=100, default="Brak")
    data = models.DateField(default=timezone.now)
    tresc = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    data_modyfikacji = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tytul

    class Meta:
        verbose_name = "Notatka"
        verbose_name_plural = "Notatki"
        ordering = ['-data']
