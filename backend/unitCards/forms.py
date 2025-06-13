from django import forms
from .models import Character, Weapon

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            'name', 'cost', 'M', 'T', 'SV', 'W', 'LD', 'OC'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.TextInput(attrs={'class': 'form-control'}),
            'M': forms.TextInput(attrs={'class': 'form-control'}),
            'T': forms.TextInput(attrs={'class': 'form-control'}),
            'SV': forms.TextInput(attrs={'class': 'form-control'}),
            'W': forms.TextInput(attrs={'class': 'form-control'}),
            'LD': forms.TextInput(attrs={'class': 'form-control'}),
            'OC': forms.TextInput(attrs={'class': 'form-control'}),
        }

class WeaponForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = [
            'character', 'name', 'range', 'A', 'WS', 'S', 'AP', 'D', 'keywords'
        ]
        widgets = {
            'character': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'range': forms.TextInput(attrs={'class': 'form-control'}),
            'A': forms.TextInput(attrs={'class': 'form-control'}),
            'WS': forms.TextInput(attrs={'class': 'form-control'}),
            'S': forms.TextInput(attrs={'class': 'form-control'}),
            'AP': forms.TextInput(attrs={'class': 'form-control'}),
            'D': forms.TextInput(attrs={'class': 'form-control'}),
            'keywords': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }