from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from registration.forms import ProfileUserCreationForm, PictureForm, Purcahse
from registration.models import ProfilePicture, Profile
import braintree

@login_required()
def profile(request):
    # lists = List.objects.filter(profile=request.user)
    # locations = Location.objects.filter(lists__profile=request.user)
    # data = {'lists': lists, 'locations': locations}
    profile_pictures = ProfilePicture.objects.filter(profile=request.user)
    picture_form = PictureForm()

    data = {'picture_form': picture_form,
            'profile_pictures': profile_pictures}
    return render(request, 'profile.html', data)


def create_purchase(request):
    client_token = braintree.ClientToken.generate({
    # "customer_id": 1
    })
    form = Purcahse({'token':client_token})
    if request.method =="POST":
        form = Purcahse(request.POST)
        if form.is_valid():
            nonce = form.clean_data["payment_method_nonce"]
        result = braintree.Transaction.sale({
            "amount": "10.00",
            "payment_method_nonce": nonce
        })
    return render(request, "create_purchase.html", {
        'form': form,
    })


        # result = braintree.Customer.create({
        #     "first_name": "Charity",
        #     "last_name": "Smith",
        #     "payment_method_nonce": nonce
        # })
        #
        # result.is_success
        # # True
        #
        # result.customer.id
        # # e.g 160923
        #
        # result.customer.credit_cards[0].token
        # Use payment method nonce here...

def register(request):
    if request.method == 'POST':
        form = ProfileUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.email_user("Welcome!", "Thank you for signing up for our website.")
            # text_content = 'Thank you, {} for signing up for our website!'.format(user.username)
            # html_content = '<h2>Thanks, {} for signing up!</h2> <div>I hope you enjoy using our site</div>'.format(user.first_name)
            # msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            return redirect("login")
    else:
        form = ProfileUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })


@login_required()
def upload_profile_picture(request):
    if request.method == 'POST':
        picture_form = PictureForm(request.POST, request.FILES)
        if picture_form.is_valid():
            pic = ProfilePicture(description=picture_form.cleaned_data['description'],
                          image=picture_form.cleaned_data['picture'],
                          profile=Profile.objects.get(id=request.user.id))
            pic.save()
        return redirect('profile')