from django.forms import ModelForm
from .models import Enrollment

class Form(ModelForm):
    class Meta:
        model = Enrollment
        fields = ['NetId', 'CRN']
