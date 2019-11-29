from django import forms
from modelformapp.models import Users
class NewUserForm(forms.ModelForm):
    class Meta:
        model=Users
        fields='__all__'
