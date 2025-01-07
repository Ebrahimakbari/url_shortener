from django import forms
from .models import UrlShortener


class UrlShortenerForm(forms.ModelForm):
    class Meta:
        model = UrlShortener
        fields = ["original_url"]
        widgets = {
            "original_url": forms.URLInput(
                attrs={"class": "form-control", "placeholder": "URL to shorten"}
            ),
        }
