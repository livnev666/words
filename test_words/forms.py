from django import forms
from .models import Text


class FileForm(forms.ModelForm):

    class Meta:

        model = Text
        fields = ['file_name']
        labels = {
            'file_name': 'Название документа'
        }


class ProfileSearchForm(forms.Form):
    name = forms.CharField(label='Поле поиска', required=False)

    # def clean(self):
    #     cleaned_data = super(ProfileSearchForm, self).clean()
    #     name = cleaned_data.get('')
    #     return self.cleaned_data.get(name)

