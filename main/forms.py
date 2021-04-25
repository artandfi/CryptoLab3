from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Message, Profile

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('__all__')
        exclude = ['sender']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Повідомлення', 'rows': 3}),
            'recipient': forms.Select(
                choices=Profile.objects.all().values_list('id', 'user')
            )
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=30,
        help_text='Required. Enter a valid email address.'
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )