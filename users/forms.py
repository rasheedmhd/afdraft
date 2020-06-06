from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


#A form to create a new user
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        User = get_user_model()
        fields = ('email', 'username',)


#A form to edit an already existing user
class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        User = get_user_model()
        fields = ('email', 'username',)