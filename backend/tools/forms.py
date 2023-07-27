from django import forms
from tools.models import WordFile


class FileForm(forms.ModelForm):
    file = forms.FileField(widget=forms.FileInput(attrs={'style':'background:indigo'}), required=False)

    class Meta:
        model = WordFile
        fields = ('file',)
