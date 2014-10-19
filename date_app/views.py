import re
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect





# ##############
# REGISTRATION #
###############
from date_app.forms import DaterCreationForm
from date_app.models import Dater


def register(request):
    if request.method == 'POST':
        form = DaterCreationForm(request.POST)
        if form.is_valid():
            # user = form.save() <<=== need this line for email but Pep8 complains about user not referenced....
            form.save()
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
    return render(request,"search.html")


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

# def search_lat_long(request, coordinates):
#     match = re.search(r'=([^&]*)&[^=]*=(.*)$',coordinates)
#     my_lat = float(match.group(1))
#     my_longi = float(match.group(2))
#     dater_list= Dater.objects.filter(latitude__range=(my_lat-.02, my_lat +.02)).filter(longitude__range=(my_longi-.02, my_longi+.02))
#     return render(request,dater_list)


#####################
# BUMP INTO MATCHES #
####################

def bump_into_matches():

    return
##################
# BUMPIN MATCHES #
##################

def bumpin_matches():

    return

###########
# PROFILE #
###########

def profile(request):

    data = {
        bump_into_matches = bump_into_matches()
        bumpin_matches = bumpin_matches
    }
    return render(request, "profile.html", data)