from django import forms
from .models import Day

class DayCreateForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = ['date_of_interview', 'name_of_company', 'what_kinda_spi', 'date_of_spi', 'resume_of_spi', 'detail_text']