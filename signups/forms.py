from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        # from models.py (see above import)
        model = SignUp