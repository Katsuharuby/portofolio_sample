from django import forms
from .models import Day
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DayCreateForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = ['date_of_interview', 'name_of_company', 'what_kinda_spi', 'date_of_spi', 'resume_of_spi', 'detail_text']
        widgets = {
            'date_of_interview': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'date_of_spi': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'resume_of_spi': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

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

class DateRangeForm(forms.Form):
    FILTER_CHOICES = [
        ('date_of_interview', '面談日付'),
        ('date_of_spi', '適性検査締切'),
        ('resume_of_spi', '履歴書提出締切'),
    ]
    
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}), 
        required=False,
        label='開始日'
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}), 
        required=False,
        label='終了日'
    )
    filter_by = forms.ChoiceField(
        choices=FILTER_CHOICES,
        required=True,
        label='絞り込み基準'
    )