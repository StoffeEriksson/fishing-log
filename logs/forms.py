from django import forms
from .models import FishingSession, Catch
from django.forms import modelformset_factory

class FishingSessionForm(forms.ModelForm):
    class Meta:
        model = FishingSession
        fields = ['location', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

CatchFormSet = modelformset_factory(
    Catch,
    fields=('species', 'count'),
    extra=1,
    can_delete=True,
    
)