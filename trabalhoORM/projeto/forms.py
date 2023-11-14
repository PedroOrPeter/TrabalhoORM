from django import forms
from .models import Voo


class VooForm(forms.ModelForm):
    class Meta:
        model = Voo
        fields = ['nome_do_voo', 'data_voo', 'hora_voo']
