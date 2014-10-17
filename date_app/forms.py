from django import forms

class SearchForm(forms.Form):
    MALE = 'M'
    FEMALE = 'F'
    CHOICES = (
        (FEMALE, 'female'),
        (MALE,'male'),
    )

    male_female = forms.ChoiceField(choices=CHOICES)
    looking_for_male_female = forms.ChoiceField(choices=CHOICES)
    # description = forms.CharField(max_length=125, widget=forms.TextInput(attrs={'class': 'form-control',
    #                                                                             'placeholder': 'description'}))