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



    def __init__(self, *args, **kwargs):
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

        gender_male = forms.TypedChoiceField(
                   coerce=lambda x: x == 'True',
                   choices=((True, 'Male'), (False, 'Female')),
                   widget=forms.RadioSelect
                )
        gender_preference_male = forms.TypedChoiceField(
                   coerce=lambda x: x == 'True',
                   choices=((True, 'Male'), (False, 'Female')),
                   widget=forms.RadioSelect
                )
        # dater = kwargs.pop('dater', None)
        super(DaterCreationForm, self).__init__(*args, **kwargs)
        self.fields['gender_male'] = gender_male
        self.fields['gender_preference_male'] = gender_preference_male
        self.fields['occupation'] = forms.ChoiceField(choices=CHOICES)
        self.fields['gender_male'].label = "Gender"
        self.fields['gender_preference_male'].label = "Gender Preference"

    class Meta:
        model = Dater
        fields = ("username", "email", "first_name", "last_name", "password1", "password2", "gender_male", "gender_preference_male", "occupation",  'age', 'height', 'weight', 'profile_image')


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