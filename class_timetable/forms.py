from django import forms
from .models import TycoInput, SycoInput, FycoInput

class TycoInputForm(forms.ModelForm):
    class Meta:
        model = TycoInput
        fields = ['subject_name', 'teacher_name', 'theory_credits', 'practical_credits']

class SycoInputForm(forms.ModelForm):
    class Meta:
        model = SycoInput
        fields = ['subject_name', 'teacher_name', 'theory_credits', 'practical_credits']

class FycoInputForm(forms.ModelForm):
    class Meta:
        model = FycoInput
        fields = ['subject_name', 'teacher_name', 'theory_credits', 'practical_credits']
