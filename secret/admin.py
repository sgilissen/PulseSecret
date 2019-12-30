from django.contrib import admin
from .models import Group, Secret
from simple_history.admin import SimpleHistoryAdmin
from .forms import SecretForm

# Register your models here.
@admin.register(Group)
class GroupAdmin(SimpleHistoryAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Secret)
class SecretAdmin(SimpleHistoryAdmin):
    list_display = ('name', 'username', 'group', 'expiry_date', 'created', 'last_modified',)
    search_fields = ['name', 'user__username']
    form = SecretForm
