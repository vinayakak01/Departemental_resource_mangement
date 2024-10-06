from django.shortcuts import render, redirect, get_object_or_404
from .models import OperatingSystem, IDE, Software
from .forms import OperatingSystemForm, IDEForm, SoftwareForm

def home(request):
    return render(request, 'licenses/home.html')

def manage_operating_systems(request):
    if request.method == 'POST':
        form = OperatingSystemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_operating_systems')
    else:
        form = OperatingSystemForm()
    operating_systems = OperatingSystem.objects.all()
    context = {
        'form': form,
        'operating_systems': operating_systems,
    }
    return render(request, 'licenses/manage_operating_systems.html', context)

def edit_operating_system(request, id):
    operating_system = get_object_or_404(OperatingSystem, id=id)
    if request.method == 'POST':
        form = OperatingSystemForm(request.POST, instance=operating_system)
        if form.is_valid():
            form.save()
            return redirect('manage_operating_systems')
    else:
        form = OperatingSystemForm(instance=operating_system)
    return render(request, 'licenses/edit_operating_system.html', {'form': form})

def delete_operating_system(request, id):
    operating_system = get_object_or_404(OperatingSystem, id=id)
    operating_system.delete()
    return redirect('manage_operating_systems')

def manage_ides(request):
    if request.method == 'POST':
        form = IDEForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_ides')
    else:
        form = IDEForm()
    ides = IDE.objects.all()
    context = {
        'form': form,
        'ides': ides,
    }
    return render(request, 'licenses/manage_ides.html', context)

def edit_ide(request, id):
    ide = get_object_or_404(IDE, id=id)
    if request.method == 'POST':
        form = IDEForm(request.POST, instance=ide)
        if form.is_valid():
            form.save()
            return redirect('manage_ides')
    else:
        form = IDEForm(instance=ide)
    return render(request, 'licenses/edit_ide.html', {'form': form})

def delete_ide(request, id):
    ide = get_object_or_404(IDE, id=id)
    ide.delete()
    return redirect('manage_ides')

def manage_softwares(request):
    if request.method == 'POST':
        form = SoftwareForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_softwares')
    else:
        form = SoftwareForm()
    softwares = Software.objects.all()
    context = {
        'form': form,
        'softwares': softwares,
    }
    return render(request, 'licenses/manage_softwares.html', context)

def edit_software(request, id):
    software = get_object_or_404(Software, id=id)
    if request.method == 'POST':
        form = SoftwareForm(request.POST, instance=software)
        if form.is_valid():
            form.save()
            return redirect('manage_softwares')
    else:
        form = SoftwareForm(instance=software)
    return render(request, 'licenses/edit_software.html', {'form': form})

def delete_software(request, id):
    software = get_object_or_404(Software, id=id)
    software.delete()
    return redirect('manage_softwares')
