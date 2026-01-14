from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import DevUser
from captcha.fields import CaptchaField


SCHEDULE_CHOICES = (
         ('OFFICE', 'OFFICE'),
        ('FLEX', 'FLEX'),
        ('REMOTE', 'REMOTE'),
)


GENDER = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
)


class CaptchaLoginForm(UserCreationForm):
  capthca = CaptchaField(label='Confirm you are not a robot')



class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    photo = forms.ImageField(required=True)
    phone = forms.CharField(max_length=15, initial='+996',required=True)
    gender = forms.ChoiceField(choices=GENDER,required=True)
    city = forms.CharField(max_length=100,required=True)
    bio = forms.CharField(max_length=500,required=True)
    github_url = forms.URLField(max_length=200,required=True)
    portfolio_file = forms.FileField(required=True)
    experience_years = forms.CharField(initial=0,required=True)
    motivation_letter = forms.CharField(max_length=1000,required=True)
    expectations = forms.CharField(max_length=300,required=True)



class Meta:
        model = DevUser
        fields = (
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',
            'photo',
            'phone',
            'gender',
            'city',
            'bio',
            'github_url',
            'portfolio_file',
            'experience_years',
            'motivation_letter',
            'expectations',
            'schedule'
        )


   
def save(self, commit = True):
        user = super(CustomRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
