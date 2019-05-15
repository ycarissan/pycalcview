from django.db import models
from django.utils import timezone

# Create your models here.

class Molecule(models.Model):
    name_text      = models.CharField('Name',    max_length=200)
    formula_text   = models.CharField('Formula', max_length=200)
    jmol_file_text = models.CharField('File',    max_length=200)
    author_text    = models.CharField('Author',  max_length=200,
                                      default='Yannick')
    "For the defaut date, pass the function and not the evaluation of the \
    function otherwise, the date will be the one of the execution of models \
    and not the one of the addition itself"
    pub_date       = models.DateTimeField('date published',
                                          default=timezone.now)

    def __str__(self):
        return self.name_text

class Vibration(models.Model):
    molecule      = models.ForeignKey(Molecule, on_delete=models.CASCADE)
    value_float   = models.FloatField('Energy')
    unit_text     = models.CharField('Unit', default="cm-1", max_length=10)
    symmetry_text = models.CharField('Symmetry', default="a", max_length=20)

    def __str__(self):
        return "{:4s} {:10.4f} {:%s}".format(self.symmetry_text, self.value_float,
                                       self.unit_text)

class Orbital(models.Model):
    molecule      = models.ForeignKey(Molecule, on_delete=models.CASCADE)
    value_float   = models.FloatField('Energy')
    unit_text     = models.CharField('Unit', default="a.u.", max_length=10)
    symmetry_text = models.CharField('Symmetry', default="a", max_length=20)

    def __str__(self):
        return "{:4s} {:10.4f} {:%s}".format(self.symmetry_text, self.value_float,
                                       self.unit_text)

