from django import forms

class Account(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', "placeholder":"First Name"}),
        max_length=30,
        required=True,
        )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', "placeholder":"First Name"}),
        max_length=30,
        required=True,
        )
    region = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', "placeholder":"Your Region e.g. Central"}),
        max_length=30,
        required=True,
        )
    tagline = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'class': 'form-control', "placeholder":"Short Bio about yourself"}),
        ) 
    source = forms.CharField(
        max_length=50,
        widget=forms.HiddenInput()
        )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        region = cleaned_data.get('region')
        tagline = cleaned_data.get('tagline')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')
        