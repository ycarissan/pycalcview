from django.contrib import admin

# Register your models here.
from .models import Molecule
from .models import Vibration
from .models import Orbital

admin.site.register(Molecule)
admin.site.register(Vibration)
admin.site.register(Orbital)
