from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Molecule


def index(request):
    latest_molecule_list = Molecule.objects.order_by('-pub_date')[:5]
    context = {'latest_molecule_list': latest_molecule_list}
    return render(request, 'viewmol/index.html', context)


def detail(request, molecule_id):
    molecule = get_object_or_404(Molecule, pk=molecule_id)
    return render(request, 'viewmol/detail.html', {'molecule': molecule})
