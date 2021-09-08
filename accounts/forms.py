# These are the built-in auth package
from django.contrib.auth.forms import UserCreationForm


# from django.contrib.auth import get_user_model
# We will replace this to account model
from accounts.models import User

class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    # when customize your auth table, it work like this
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['username'].label = 'Display Name'
    #     self.fields['email'].label = "Email Address"

    # And we will try to customize form as learn previous

    