from django import forms
from .models import Day
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DayCreateForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = ['date_of_interview', 'name_of_company', 'what_kinda_spi', 'date_of_spi', 'resume_of_spi', 'detail_text']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user