from django import forms #eisagagw tis formes tou django wste na mporw na to epe3ergastw
from django.contrib.auth.models import User #eisagagw to montelo tou User (tou django)
from django.contrib.auth.forms import UserCreationForm #eisagagw thn automath forma tou django
from users.models import Profile

class UserRegistrationForm(UserCreationForm): #ftiaxnw mia class UserRegistrationForm opou pairnei thn 
                                                #form UserCreationFrom
    email = forms.EmailField()                  #EmailField (default einai na einai required opote afhnw kenes paren9eseis)

    class Meta():
        model = User #pairnw to montelo User tou django
        fields = ['username','email', 'password1', 'password2'] #vazw ta pedia p 9elw na exei
        #na pros9esw kai ta pedia firstname lastname (na ele3w sthn db pws einai kanonika)

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
        
    class Meta():
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta():
        model = Profile
        fields = ['photoprofile']