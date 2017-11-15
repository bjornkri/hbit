from django import forms

from actions.models import Action


class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ['description']
