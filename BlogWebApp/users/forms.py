from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from users.models import Profile

class userRegisterForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
#user updateform for user information
class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
#user profile update for image 
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']