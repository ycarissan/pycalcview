from django.core.management.base import BaseCommand
from viewmol.models import Molecule, Vibration, Orbital

class Command(BaseCommand):
    args = 'name="NAME" formula="CnHn.."'
    help = "Add molecule with name NAME and formula FORMULA"

    def add_arguments(self, parser):
        parser.add_argument('name')
        parser.add_argument('formula')
        parser.add_argument('path')

    def _create_molecule(self, name, formula):
        mol = Molecule(name_text      = name       , \
                       formula_text   = formula)
        mol.save()
        return mol

    def _create_vibration(molecule, vibration):
        return

    def get_vibrations(path):
        return

    def handle(self, *args, **kwargs):
        name=kwargs['name']
        formula=kwargs['formula']
        path=kwargs['path']
        molecule = self._create_molecule(name=name, formula=formula)
        vibrations = get_vibrations(path)
        for vib in vibrations:
            self._create_vibration(molecule, vib)

