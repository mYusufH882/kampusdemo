# from django.forms import ModelForm
from django import forms

from .models import Fakultas


class FakultasForm(forms.Form):
    nama_fakultas = forms.CharField(
        label="Nama Fakultas", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    prodi = forms.CharField(
        label="Program Studi", widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Fakultas

        fields = ("nama_fakultas", "prodi")
