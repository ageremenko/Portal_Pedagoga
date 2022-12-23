from django.forms import ModelForm
from demoapp.models import Data


class DataForm(ModelForm):
    class Meta:
        model = Data
        fields = ['category', 'quantity']