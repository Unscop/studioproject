from django import forms
from .models import CallBack

class CallBackForm(forms.ModelForm):
 
    class Meta:
        model = CallBack
        fields = ['email']

        def clean_email(self):
            email = self.cleaned_data.get('email')
            return email
        # model = CallBack
        # fields = '__all__'
        # fields = ("name", "email", "message",)
        # widgets = {
        #     "name":forms.TextInput(attrs={'class': 'comment-name','placeholder': 'Name*'}),
        #     "email":forms.EmailInput(attrs={'class': 'comment-email','placeholder': 'Email*'}),
        #     "message":forms.TextInput(attrs={'class': 'comment-message', 'placeholder': 'Message...'})
        # }
        