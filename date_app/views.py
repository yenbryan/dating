from django.shortcuts import render, redirect
from date_app.forms import SearchForm
from registration.forms import ProfileUserCreationForm
from registration.models import Profile


def home(request):
    # if request.user.is_authenticated():
    #     return redirect('profile')

    return render(request, 'home.html', {'search_form': SearchForm()})


def matches(request):
    if request.method=='POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            male_female = search_form.cleaned_data['male_female']
            looking_for_male_female = search_form.cleaned_data['looking_for_male_female']
            profiles = Profile.objects.filter(male_female=looking_for_male_female,
                                              looking_for_male_female=male_female)
            profile_creation = ProfileUserCreationForm({'male_female':looking_for_male_female,
                                                        'looking_for_male_female':male_female})
            data = {'profiles': profiles, 'profile_creation': profile_creation}
            return render(request,'matches.html', data)
    return redirect('home')