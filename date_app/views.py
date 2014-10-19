from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect





# ##############
# REGISTRATION #
###############
from date_app.forms import DaterCreationForm


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
            return redirect("home")

    else:
        form = DaterCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

########
# HOME #
########

def home(request):
    return render(request, "home.html")