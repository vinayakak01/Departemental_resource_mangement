from django import forms
from .models import OperatingSystem, IDE, Software

class OperatingSystemForm(forms.ModelForm):
    class Meta:
        model = OperatingSystem
        fields = ['name', 'version', 'license_type', 'date_purchased', 'valid_upto', 'price']
        widgets = {
            'date_purchased': forms.DateInput(attrs={'type': 'date'}),
            'valid_upto': forms.DateInput(attrs={'type': 'date'}),
        }

class IDEForm(forms.ModelForm):
    class Meta:
        model = IDE
        fields = ['name', 'version', 'license_type', 'date_purchased', 'valid_upto', 'price']
        widgets = {
            'date_purchased': forms.DateInput(attrs={'type': 'date'}),
            'valid_upto': forms.DateInput(attrs={'type': 'date'}),
        }

class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = ['name', 'version', 'license_type', 'date_purchased', 'valid_upto', 'price']
        widgets = {
            'date_purchased': forms.DateInput(attrs={'type': 'date'}),
            'valid_upto': forms.DateInput(attrs={'type': 'date'}),
        }
