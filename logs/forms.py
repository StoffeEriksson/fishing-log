from django import forms
from .models import FishLog

class FishLogForm(forms.ModelForm):
    class Meta:
        model = FishLog
        fields = ['location', 'fish_count']