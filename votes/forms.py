from django import forms
from .models import *


class QuestForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = "__all__"