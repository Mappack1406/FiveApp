from cProfile import label
from email.policy import default
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from django.contrib import messages
from pkg_resources import require
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

from .models import AusstiegAmb

#becomes auth_user in sqlite3
class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=50)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

#becomes main_AusstiegAmb in sqlite3
class CreateAusstiegAbmulanz(ModelForm):
    class Meta:
        model = AusstiegAmb
        fields = ['name', 'schriftlichepruefung', 'muendlichepruefung', 'akten_abgegeben', 'therapeutenornder_fertiggestellt',
        'vorname','festplatte_abgegeben','schluessel_abgegeben','schließfach_geprueft','tuerchip_abgegeben',
        'tuerschild_abgegeben','namensschild_abgegeben','versicherung_abgemeldet','fachkonverenz_ausgetragen',
        'email_verteilerlisten_entfernt','dauerbuchung_geloescht','Staatspruefungstermine_eingetragen','Fiona_auf_beendet',
        'festplatte_geloescht','pc_account_deaktiviert','pia_zugang_deaktiviert','email_gelöscht']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 240px;',
                'placeholder': 'Name'
                }),
            'vorname': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 240px;',
                'placeholder': 'Vorname'
                }),
            'schriftlichepruefung': forms.SelectDateWidget(years=range(2014,2030)),
            'muendlichepruefung': forms.SelectDateWidget(years=range(2014,2030)),
            'akten_abgegeben': forms.SelectDateWidget(years=range(2014,2030)),
            'therapeutenornder_fertiggestellt': forms.SelectDateWidget(years=range(2014,2030)),
            'festplatte_abgegeben': forms.SelectDateWidget(years=range(2014,2030)),
            'schluessel_abgegeben': forms.SelectDateWidget(years=range(2014,2030)),
            'schließfach_geprueft': forms.SelectDateWidget(years=range(2014,2030)),
            'tuerchip_abgegeben': forms.SelectDateWidget(years=range(2014,2030)),
            'tuerschild_abgegeben': forms.SelectDateWidget(years=range(2014,2030)),
            'namensschild_abgegeben': forms.SelectDateWidget(years=range(2014,2030)),
            'versicherung_abgemeldet': forms.SelectDateWidget(years=range(2014,2030)),
            'fachkonverenz_ausgetragen': forms.SelectDateWidget(years=range(2014,2030)),
            'email_verteilerlisten_entfernt': forms.SelectDateWidget(years=range(2014,2030)),
            'dauerbuchung_geloescht': forms.SelectDateWidget(years=range(2014,2030)),
            'Staatspruefungstermine_eingetragen': forms.SelectDateWidget(years=range(2014,2030)),
            'Fiona_auf_beendet': forms.SelectDateWidget(years=range(2014,2030)),
            'festplatte_geloescht': forms.SelectDateWidget(years=range(2014,2030)),
            'pc_account_deaktiviert': forms.SelectDateWidget(years=range(2014,2030)),
            'pia_zugang_deaktiviert': forms.SelectDateWidget(years=range(2014,2030)),
            'email_gelöscht': forms.SelectDateWidget(years=range(2014,2030))
        }
    def save(self, *args, **kwargs):
        post = AusstiegAmb.objects.create(
            user = kwargs.pop('user'),
            vorname = self.cleaned_data['vorname'],
            name = self.cleaned_data['name'],
            schriftlichepruefung = self.cleaned_data['schriftlichepruefung'],
            muendlichepruefung = self.cleaned_data['muendlichepruefung'],
            akten_abgegeben = self.cleaned_data['akten_abgegeben'],
            therapeutenornder_fertiggestellt = self.cleaned_data['therapeutenornder_fertiggestellt'],
            festplatte_abgegeben = self.cleaned_data['festplatte_abgegeben'],
            schluessel_abgegeben = self.cleaned_data['schluessel_abgegeben'],
            schließfach_geprueft = self.cleaned_data['schließfach_geprueft'],
            tuerchip_abgegeben = self.cleaned_data['tuerchip_abgegeben'],
            tuerschild_abgegeben = self.cleaned_data['tuerschild_abgegeben'],
            namensschild_abgegeben = self.cleaned_data['namensschild_abgegeben'],
            versicherung_abgemeldet = self.cleaned_data['versicherung_abgemeldet'],
            fachkonverenz_ausgetragen = self.cleaned_data['fachkonverenz_ausgetragen'],
            email_verteilerlisten_entfernt = self.cleaned_data['email_verteilerlisten_entfernt'],
            dauerbuchung_geloescht = self.cleaned_data['dauerbuchung_geloescht'],
            Staatspruefungstermine_eingetragen = self.cleaned_data['Staatspruefungstermine_eingetragen'],
            Fiona_auf_beendet = self.cleaned_data['Fiona_auf_beendet'],
            festplatte_geloescht = self.cleaned_data['festplatte_geloescht'],
            pc_account_deaktiviert = self.cleaned_data['pc_account_deaktiviert'],
            pia_zugang_deaktiviert = self.cleaned_data['pia_zugang_deaktiviert'],
            email_gelöscht = self.cleaned_data['email_gelöscht']
        )
        return post