from django import forms
from django.forms import ModelForm
from .models import Pro


class ProForm(ModelForm):

    class Meta:
        model = Pro
        fields = ['nombre', 'precio', 'stock', 'foto', 'categoria']

 







