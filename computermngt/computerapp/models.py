from django.db import models

# Create your models here.

class Machine(models.Model):
    id = models.AutoField(
        primary_key = True,
        editable = False
    )
    nom = models.CharField(
        max_length = 6
    )

    def __str__(self):
        return str(self.id) + " " + self.nom
    
    def get_name(self):
        return str(self.id) + " " + self.nom