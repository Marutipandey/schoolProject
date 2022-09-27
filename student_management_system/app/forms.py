from dataclasses import fields
from pyexpat import model
from django import forms
from .models import studentDetails
class studentDetailsForms(forms.ModelForm):
    class Meta:
        model=studentDetails
        fields=['Name','Father_name','Mother_name','Email','Class','Contact_number','Address']
        widgets={
        'Name':forms.TextInput(attrs={'class':'form-control'}),
        'Father_name':forms.TextInput(attrs={'class':'form-control'}),
        'Mother_name':forms.TextInput(attrs={'class':'form-control'}),
        'Email':forms.EmailInput(attrs={'class':'form-control'}),
        'Class':forms.NumberInput(attrs={'class':'form-control'}),
        'Contact_number':forms.NumberInput(attrs={'class':'form-control'}),
        'Address':forms.TextInput(attrs={'class':'form-control'}),

        
        }