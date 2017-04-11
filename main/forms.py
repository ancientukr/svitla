from django.forms import ModelForm, DateInput
from main.models import Recall

class RecallForm(ModelForm):

    class Meta:
        model = Recall
        fields = ['name','email', 'social', 'type_photo', 'location', 'massage', 'info_about_my']
        widgets = {
            'date_photo_shooting': DateInput(format='%d/%m/%Y'),
        }
