from django import forms
from ejemplo.models import Familiar, Automovil, Mascota

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Busque algo..'}))

class BuscarAutomoviles(forms.Form):
    marca = forms.CharField(max_length=100)

class BuscarMascotas(forms.Form):
    nombre = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']

class AutomovilForm(forms.ModelForm):
  class Meta:
    model = Automovil
    fields = ['marca', 'modelo', 'año']

class MascotaForm(forms.ModelForm):
  class Meta:
    model = Mascota
    fields = ['nombre', 'raza', 'edad']