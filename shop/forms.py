from django import forms

from shop.models import Honey


class HoneyForm(forms.ModelForm):
    class Meta:
        model = Honey
        fields = '__all__'
