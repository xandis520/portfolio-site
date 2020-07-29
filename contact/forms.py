from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput(attrs={
        'class': 'email',
        'placeholder': 'Your email',
    }))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'subject',
        'placeholder': 'Subject',
    }))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'message',
        'placeholder': 'Message',
    }))
