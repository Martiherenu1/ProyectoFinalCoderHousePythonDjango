from django import forms
from .models import Turno

class TurnoForm(forms.ModelForm):
    hora = forms.TimeField(widget=forms.Select(attrs={'class': 'form-select', 'id': 'id_hora'}))

    class Meta:
        model = Turno
        fields = ['servicio', 'fecha', 'hora', 'metodo_pago']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'id_fecha'}),
            'servicio': forms.Select(attrs={'class': 'form-select'}),
            'metodo_pago': forms.Select(attrs={'class': 'form-select'}),
        }
