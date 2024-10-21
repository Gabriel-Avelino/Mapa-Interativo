from django.db import models

# Create your models here.
class Horario(models.Model):
    address = models.CharField(max_length=256, null=True)
    segunda_diurno = models.TimeField(null=True, blank=True)
    segunda_noturno = models.TimeField(null=True, blank=True)
    terca_diurno = models.TimeField(null=True, blank=True)
    terca_noturno = models.TimeField(null=True, blank=True)
    quarta_diurno = models.TimeField(null=True, blank=True)
    quarta_noturno = models.TimeField(null=True, blank=True)
    quinta_diurno = models.TimeField(null=True, blank=True)
    quinta_noturno = models.TimeField(null=True, blank=True)
    sexta_diurno = models.TimeField(null=True, blank=True)
    sexta_noturno = models.TimeField(null=True, blank=True)
    sabado_diurno = models.TimeField(null=True, blank=True)
    sabado_noturno = models.TimeField(null=True, blank=True)
    domingo_diurno = models.TimeField(null=True, blank=True)
    domingo_noturno = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.address