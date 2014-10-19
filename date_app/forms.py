from django.contrib.auth.forms import UserCreationForm
from django import forms
from models import Dater

#django crispy forms:
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class DaterCreationForm(UserCreationForm):
    helper = FormHelper()
    helper.form_method = "POST"
    helper.form_class = 'form-horizontal'
    helper.add_input(Submit('Register', 'Register', css_class='btn-default'))

    # MALE = 'M'
    # FEMALE = 'F'
    # CHOICES = (
    #     (FEMALE, 'female'),
    #     (MALE,'male'),
    # )
    # male_female = forms.ChoiceField(choices=CHOICES)
    # looking_for_male_female = forms.ChoiceField(choices=CHOICES)

    MEDICAL_INDUSTRY = 'doctor'
    TECH = 'tech'
    STUDENT = 'Student'
    BUSINESS = 'Business'
    LAW = 'Law'
    TEACHING = 'Teaching'

    CHOICES = (
        (MEDICAL_INDUSTRY, 'Medical Industry'),
        (TECH, 'Tech'),
        (STUDENT,'Student'),
        (BUSINESS, 'Business'),
        (LAW, 'Law'),
        (TEACHING, 'Teaching'),
    )

    ocupation_choices = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = Dater
        fields = ("username", "email", "first_name", "last_name", "password1", "password2", 'age', 'height', 'weight', 'profile_image')

    # ADD: Gender, Gender Preference, how to upload image, how to set occupation_choices to the occupation field


    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            Dater.objects.get(username=username)
        except Dater.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )






# class SearchForm(forms.Form):
#     MALE = 'M'
#     FEMALE = 'F'
#     CHOICES = (
#         (FEMALE, 'female'),
#         (MALE,'male'),
#     )
#
#     male_female = forms.ChoiceField(choices=CHOICES)
#     looking_for_male_female = forms.ChoiceField(choices=CHOICES)
#     # description = forms.CharField(max_length=125, widget=forms.TextInput(attrs={'class': 'form-control',
#     #                                                                             'placeholder': 'description'}))