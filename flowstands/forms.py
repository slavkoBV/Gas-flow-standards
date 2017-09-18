# -*- coding: utf-8 -*-

from django import forms


default_text = u'Назва еталона або власника'

class SearchForm(forms.Form):
    q = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'id': 'search',
            'class': 'form-control',
            'placeholder': default_text
        })
    )