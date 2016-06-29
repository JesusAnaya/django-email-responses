from django import forms
from .models import Response


class ResponseForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'mceEditor'}))

    class Meta:
        model = Response
        fields = (
            'token',
            'from_address',
            'alternative_from',
            'subject',
            'content'
        )
