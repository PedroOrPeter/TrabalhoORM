from django.db import models

class Voo(models.Model):
    nome_do_voo = models.CharField(max_length=100)
    data_voo = models.IntegerField()
    hora_voo = models.TimeField(auto_now_add=False)

    def __str__(self):
        return self.nome_do_voo
