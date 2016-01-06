from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'message')


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea())

    def clean_name(self):
        data = self.cleaned_data['name'] # dane sprawdzone jako ok
        if "D" not in data:
            raise forms.ValidationError("Musisz mieć imie zaczynające się na 'D'!")
        return data
