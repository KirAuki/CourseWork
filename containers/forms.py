from django import forms
from .models import Container


class AddContainerForm(forms.ModelForm):
    
    class Meta:
        model = Container
        fields = "__all__"