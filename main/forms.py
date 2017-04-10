from django import forms
from main.models import Recall

class RecallForm(forms.Form):
    CATEGORIES_PHOTO_TYPE = (
        ("Wedding", "свадебная"),
        ("Pregnancy", "беременность"),
        ("Family-photo", "семейная/детская"),
        ("Love-Story", "love story"),
        ("Other", "другая")
    )

    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    social = forms.CharField(max_length=60)
    type_photo = forms.ChoiceField( choices=CATEGORIES_PHOTO_TYPE)
    date_photo_shooting = forms.DateField()
    location = forms.CharField(max_length=30)
    massage = forms.CharField(widget=forms.Textarea, max_length=1000)
    info_about_my = forms.CharField(max_length=50)


    class Meta:
        model = Recall

        field = ('name','email', 'social', 'type_photo', 'date_photo_shooting', 'location', 'massage', 'info_about_my')
