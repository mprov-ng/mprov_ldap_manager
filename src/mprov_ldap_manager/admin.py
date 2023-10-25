# -*- coding: utf-8 -*-
# https://github.com/django-ldapdb/django-ldapdb/tree/master/examples
# This software is distributed under the two-clause BSD license.
# Copyright (c) The django-ldapdb project


from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import LdapGroup, LdapUser
from django.forms import ModelForm, PasswordInput

class LdapUserForm(ModelForm):
    password = forms.CharField(widget=PasswordInput(),required=False, help_text="To remain unchanged, leave blank")
    class Meta:
        model = LdapUser
        exclude = ['dn', 'photo'] 
    def clean(self):
        data = self.cleaned_data
        if 'password' in data:
            password = data['password']
            if not password or password == "":
                del data['password']
        return data

class LdapUserAdmin(admin.ModelAdmin):
    form = LdapUserForm
    exclude = ['dn', 'photo', 'full_name', 'gecos']
    list_display = ['username', 'first_name', 'last_name', 'email', 'uid']
    readonly_fields = ['last_password_change']
    search_fields = ['first_name', 'last_name', 'full_name', 'username']


class LdapGroupForm(forms.ModelForm):
    usernames = forms.ModelMultipleChoiceField(
        queryset=LdapUser.objects.all(),
        widget=FilteredSelectMultiple('Users', is_stacked=False),
        required=False,
    )

    class Meta:
        exclude = []
        model = LdapGroup

    def clean_usernames(self):
        data = self.cleaned_data['usernames']
        if not data:
            return []
        return list(data.values_list('username', flat=True))


class LdapGroupAdmin(admin.ModelAdmin):
    form = LdapGroupForm
    exclude = ['dn', 'usernames', 'member']
    list_display = ['name', 'gid']
    search_fields = ['name']

class LdapServerAdmin(admin.ModelAdmin):
    pass

admin.site.register(LdapGroup, LdapGroupAdmin)
admin.site.register(LdapUser, LdapUserAdmin)