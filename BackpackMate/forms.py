from django import forms
from .models import District

class PlaceFilterForm(forms.Form):
    district = forms.ModelChoiceField(queryset=District.objects.all(), required=False)
    category = forms.ChoiceField(choices=[
        ('temple', 'Temple'),
        ('heritage', 'Heritage'),
        ('beach', 'Beach'),
        ('tourism', 'Tourism Spot'),
    ], required=False)
