from django.db import models


# Create your models here.

class Molecule(models.Model):
    name_text = models.CharField('Name', max_length=200)
    formula_text = models.CharField('Formula', max_length=200)
    jmol_file_text = models.CharField('File', max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name_text
