from asyncio.windows_events import NULL
from xml.dom.pulldom import default_bufsize
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class AusstiegAmb(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    schriftlichepruefung = models.DateTimeField(default=timezone.now)
    muendlichepruefung = models.DateTimeField(default=timezone.now)
    akten_abgegeben = models.DateTimeField(default=timezone.now)
    therapeutenornder_fertiggestellt = models.DateTimeField(default=timezone.now)
    festplatte_abgegeben = models.DateTimeField(default=timezone.now)
    schluessel_abgegeben = models.DateTimeField(default=timezone.now)
    schließfach_geprueft = models.DateTimeField(default=timezone.now)
    tuerchip_abgegeben = models.DateTimeField(default=timezone.now)
    tuerschild_abgegeben = models.DateTimeField(default=timezone.now)
    namensschild_abgegeben = models.DateTimeField(default=timezone.now)
    versicherung_abgemeldet = models.DateTimeField(default=timezone.now)
    fachkonverenz_ausgetragen = models.DateTimeField(default=timezone.now)
    email_verteilerlisten_entfernt = models.DateTimeField(default=timezone.now)
    dauerbuchung_geloescht = models.DateTimeField(default=timezone.now)
    Staatspruefungstermine_eingetragen = models.DateTimeField(default=timezone.now)
    Fiona_auf_beendet = models.DateTimeField(default=timezone.now)
    festplatte_geloescht = models.DateTimeField(default=timezone.now)
    pc_account_deaktiviert = models.DateTimeField(default=timezone.now)
    pia_zugang_deaktiviert = models.DateTimeField(default=timezone.now)
    email_gelöscht = models.DateTimeField(default=timezone.now)
    vorname = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

