from django import forms


class ShortLinkForm(forms.Form):
    url = forms.URLField()
