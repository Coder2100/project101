from django import forms
#bringing in the Contact model from models
from .models import Contact

#creating form to accept user information when contacting us
class ContactForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Name ...'}
    ),)
    email = forms.EmailField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email Address...',
        }),)
    subject = forms.CharField(label='',
    widget = forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'What is your question about?'
        }
    ),)
    message = forms.CharField(label='',
    widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Please Write Your Message...'
        }
    ),)

    class Meta:
        model = Contact
        fields = ['name', 'email','subject', 'message']
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        subject = cleaned_data.get('subject')
        message = cleaned_data.get('message')

 