from django import forms
from django.core import validators
class FormName(forms.Form):
    name=forms.CharField()
    # name=forms.CharField(validators=[checkforz])
    email=forms.EmailField()
    verifyemail=forms.EmailField(label='Enter your email again')
    text=forms.CharField(widget=forms.Textarea)

    # botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
# cleaned_data
    def clean(self):
        all_clean_data=super().clean()
        eml=all_clean_data['email']
        vmail=all_clean_data['verifyemail']
        if eml!=vmail:
            raise forms.ValidationError("Emails dont match")
    # another form of validation
    # def checkforz(value):
    #     if value[0]!='z':
    #         raise forms.ValidationError("Need to Start with Z")

# old kinda validations
    # def clean_botcatcher(self):
    #     botcatcher=self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("Gotcha")
    # return botcatcher
