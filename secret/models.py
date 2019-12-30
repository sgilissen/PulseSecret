from django.db import models
from django.forms import ModelForm, PasswordInput
from simple_history.models import HistoricalRecords


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=40)
    history = HistoricalRecords()
    changed_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class Secret(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=250)
    URL = models.URLField(blank=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.name} - {self.username}"
