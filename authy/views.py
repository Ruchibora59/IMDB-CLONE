from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from authy.models import Profile
from authy.forms import SignupForm, ChangePasswordForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
# Create your views here.
 
def Signup(request):

    if request.method == 'POST':

        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
            return redirect('login')

    else:
        form = SignupForm()       

    context = {  
        'form' : form,

    }    

    return render(request,'Registration/signup.html', context)


def PasswordChange(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            return redirect('changepassworddone')

    else:
        form = ChangePasswordForm(instance=user)

    context = {  
        'form' : form,

    }    

    return render(request,'Registration/changepassword.html', context)    


def PasswordChangeDone(request):
    return render(request,'Registration/changepassworddone.html')


@login_required
def EditProfile(request):
    user = request.user.id
    profile = Profile.objects.get(user_id=user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile.picture = form.cleaned_data.get('picture')
            profile.first_name = form.cleaned_data.get('first_name')
            profile.last_name = form.cleaned_data.get('last_name')
            profile.location =  form.cleaned_data.get('location ')
            profile.url = form.cleaned_data.get('url')
            profile.profile_info = form.cleaned_data.get('profile_info')
            profile.save()
            return redirect('index')

    else:
        form = EditProfileForm()


    context = {
        'form' : form,
    }  

    return render(request, 'editprofile.html', context)









