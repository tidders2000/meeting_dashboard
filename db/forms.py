from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class add_risk(forms.ModelForm):
    class Meta:
        model = Risk
        fields = ('__all__')


class add_actions(forms.ModelForm):
    class Meta:
        model = Action
        fields = ('__all__')
        widgets = {
            'date_complete': DateInput(),
        }


class add_issues(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('__all__')
        widgets = {
            'date_complete': DateInput(),
        }


class add_rag(forms.ModelForm):
    class Meta:
        model = Rag
        fields = ('__all__')


class add_finance(forms.ModelForm):
    class Meta:
        model = Finance
        fields = ('__all__')


class add_hr(forms.ModelForm):
    class Meta:
        model = Hr
        fields = ('__all__')
