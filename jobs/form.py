from django import forms

from .models import StoryDetail


class StoryDetailForm(forms.ModelForm):
    class Meta:
        model = ProjectDetail
        fields = '__all__'
        exclude = ('id',)
