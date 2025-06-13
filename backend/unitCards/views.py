from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CharacterForm, WeaponForm

# Create your views here.
def create_character(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('character_list')  # Replace with your own redirect
    else:
        form = CharacterForm()
    return render(request, 'create_character.html', {'form': form})

def create_weapon(request):
    if request.method == 'POST':
        form = WeaponForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('weapon_list')  # Replace with your own redirect
    else:
        form = WeaponForm()
    return render(request, 'create_weapon.html', {'form': form})