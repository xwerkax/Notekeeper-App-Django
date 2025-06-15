from django.db import models
from django.utils import timezone


class Notatka(models.Model):
    tytul = models.CharField(max_length=200)
    przedmiot = models.CharField(max_length=100, default="Brak")
    data = models.DateField(default=timezone.now)
    tresc = models.TextField()


    def __str__(self):
        return self.tytul
