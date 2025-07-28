from django.db import models

class Programme(models.Model):
    classe = models.CharField(max_length=10)  # ex: 6e, 4e, etc.
    matiere = models.CharField(max_length=100)  # ex: Mathématiques
    chapitre = models.CharField(max_length=255)  # ex: Calcul littéral
    periode = models.CharField(max_length=100)  # ex: Semaine 4
    num_chapitre = models.PositiveIntegerField()  # ex: 1, 2, 3...

    def __str__(self):
        return f"{self.classe} | {self.matiere} | {self.periode} | Ch. {self.num_chapitre} - {self.chapitre}"
