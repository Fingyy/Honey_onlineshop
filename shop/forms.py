from django import forms
from django.forms import TextInput, Textarea, FileInput, NumberInput

from shop.models import Honey, Packaging, HoneyProductOnStock


class HoneyForm(forms.ModelForm):
    class Meta:
        model = Honey
        fields = ['name', 'description', 'image']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'image': FileInput(attrs={'class': 'form-control'}),
        }


class PackagingForm(forms.ModelForm):
    class Meta:
        model = Packaging
        fields = '__all__'


class HoneyProductOnStockForm(forms.ModelForm):
    class Meta:
        model = HoneyProductOnStock
        fields = ['honey_name', 'honey_packaging', 'quantity']
        # widgets = {
        #     'honey_name': TextInput(attrs={'class': 'form-control'}),
        #     'honey_packaging': TextInput(attrs={'class': 'form-control'}),
        #     'quantity': NumberInput(attrs={'class': 'form-control'}),
        # }
