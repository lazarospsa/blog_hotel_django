from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm #automath forma gia register
from django.contrib import messages #gia mhnumata sto template
from users.forms import UserRegistrationForm #h forma p eftia3a
from django.contrib.auth.decorators import login_required #to @login_required elegxei na episkeptontai mia selida mono oi sundedemenoi xrhstes
from users.forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST) <- htan etsi kai to alla3a se UserRegistrationForm (from user.forms import UserRegistrationFrom) gia na parei ta pedia p 9elw egw
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
            '''
        else:
            username = form.cleaned_data.get('username')
            messages.warning(request, f'Account did not created for {username}')
            return redirect('register')
            '''
    else:
        #form = UserCreationForm() <- htan etsi kai to alla3a se UserRegistrationForm gia na parei ta pedia p 9elw egw
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

'''
messages.debug
messages.info
messages.success
messages.warning
messages.error
'''

'''
Update profile infos
'''
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user) #user info update form
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) #profile info update form
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user) #user info update form
        p_form = ProfileUpdateForm(instance=request.user.profile) #profile info update form
    
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'users/profile.html', context)