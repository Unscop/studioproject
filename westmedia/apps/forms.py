from django import forms
from .models import CallBack
# from snowpenguin.django.recaptcha3.fields import ReCaptchaField

class CallBackForm(forms.ModelForm):
    class Meta:
        model = CallBack
        fields = ['email']

        def clean_email(self):
            email = self.cleaned_data.get('email')
            return email
        # def clean_captcha(self):
        #     captcha = self.cleaned_data.get('captcha')
        #     return captcha
        