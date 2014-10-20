import re
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect





# ##############
# REGISTRATION #
###############
from django.views.decorators.csrf import csrf_exempt
from date_app.forms import DaterCreationForm
from date_app.models import Dater, Match


def register(request):
    if request.method == 'POST':
        form = DaterCreationForm(request.POST, request.FILES)
        if form.is_valid():
            # user = form.save() <<=== need this line for email but Pep8 complains about user not referenced....
            if form.save():
                # text_content = 'Thank you for signing up for our website, {}'.format(user.username)
                # html_content = '<h2>Thanks {} {} for signing up!</h2>
                # <div>You joined at {}.  I hope you enjoy using our site</div>'
                # .format(user.first_name, user.last_name, user.date_joined)
                # msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
                # msg.attach_alternative(html_content, "text/html")
                # msg.send()
                new_user = authenticate(username=request.POST['username'],
                                        password=request.POST['password1'])
                login(request, new_user)
                return redirect("search")
    else:
        form = DaterCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })


##########
# SEARCH #
##########

#Search for Dater's current location
# @login_required()
def search(request):
    return render(request, "search.html")

@csrf_exempt
def save_lat_long(request):
    if request.method == "POST":
        dater = Dater.objects.get(pk=request.user.pk)
        my_lat = float(request.POST['lat'])
        my_long = float(request.POST['long'])
        dater.latitude = my_lat
        dater.longitude = my_long
        dater.save()
        return redirect('profile')


#Set the Dater's location
def set_lat_long(request, coordinates):
    dater = Dater.objects.get(pk=request.user.pk)
    match = re.search(r'=([^&]*)&[^=]*=(.*)$',coordinates)
    my_lat = float(match.group(1))
    my_long = float(match.group(2))
    dater.latitude = my_lat
    dater.longitude = my_long
    dater.save()
    return profile(request)

# def search_match(request):
#     my_lat = request.user.latitude
#     my_longi = request.user.longitude
#     bump_into_matches = Match.objects.filter(user1=user, user1_select=1, user2_select=1)
#     dater_list= Dater.objects.filter(latitude__range=(my_lat-.02, my_lat +.02)).\
#         filter(longitude__range=(my_longi-.02, my_longi+.02)).exclude(id=request.user.id)
#     return render(request,'search_match.html', {'dater_list': dater_list})
#

#####################
# BUMP INTO MATCHES #
####################

def bump_into_matches(user):
    bump_into_matches = Match.objects.filter(user1=user, user1_select=1, user2_select=1)
    return bump_into_matches  #returns filtered match objects

##################
# BUMPIN MATCHES #
##################

def bumpin_matches(user):
    bumpin_matches = Match.objects.filter(user1=user, user1_select=3, user2_select=3)
    return bumpin_matches #returns filtered match objects

###########
# PROFILE #
###########

def profile(request):
    dater = request.user

    data = {
        'bump_into_matches':bump_into_matches(dater),
        'bumpin_matches': bumpin_matches(dater),
    }

    return render(request, "profile.html", data)

def dater_profile(request, dater_id):
    data = {
        'dater': Dater.objects.get(pk=dater_id)
    }
    return render(request, "date_profile.html", data)

###############
# Date Search #
###############

def date_search(request,i): #what other data
    user = request.user
    i = int(i)
    #first filter on location within set radius
    # Dater.objects.filter(latitude__range=(user.latitude -.02, user.latitude +.02)).filter(longitude__range=(user.longitude -.02, user.longitude +.02))

    #filter database based on user1 preferences and the gender of user2
    # Dater.objects.filter(gender_male=user.gender_preference_male)

    #once user2s are filtered down, then filter on their gender preference, if their gender preference is user1's preference then keep
    # Dater.objects.filter(gender_preference_male=user.gender_male)
    dater_list= Dater.objects.filter(latitude__range=(user.latitude -.02, user.latitude +.02))\
        .filter(longitude__range=(user.longitude -.02, user.longitude +.02))\
        .filter(gender_male=user.gender_preference_male)\
        .filter(gender_preference_male=user.gender_male).exclude(id=user.id)

    #remove matches which user has already seen
    match_list = []
    for user2 in dater_list:
        if not Match.objects.filter(user1=user, user2=user2, user1_select__isnull=True).exists():
            match_list.append(user2)

    data = {
        'user2': match_list[i],
        'i': i+1,
        'match_list': match_list,
    }
    return render(request, "date_search.html", data)
