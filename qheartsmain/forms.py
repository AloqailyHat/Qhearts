# qheartsmain/forms.py

from django import forms
from .models import RescueReport

class RescueReportForm(forms.ModelForm):
    class Meta:
        model = RescueReport
        fields = [
            'name',
            'mobile',
            'email',
            'address',
            'situation',
            'picture',
            'video',
            'animal_type',
            'behavior',
            'keep_at_place',
            'bring_to_shelter',
            'adopt_after_treatment',
        ]


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    phone_number = forms.CharField(max_length=15, label="Your Phone Number")
    message = forms.CharField(widget=forms.Textarea, label="Your Message")
