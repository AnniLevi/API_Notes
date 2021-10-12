from django import forms
from .models import City, Specialty


class FindVacancyForm(forms.Form):
    city = forms.ModelChoiceField(
        label='Город', queryset=City.objects.all(), to_field_name="slug",
        widget=forms.Select(attrs={'class': 'form-control'}))
    specialty = forms.ModelChoiceField(
        label='Специальность', queryset=Specialty.objects.all(),
        to_field_name="slug",
        widget=forms.Select(attrs={'class': 'form-control'}))
    # specialty = forms.CharField(
    #     label='Специальность',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Введите специальность'
    #     })
    # )
