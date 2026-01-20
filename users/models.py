from django.db import models
from django.contrib.auth.models import User


class DevUser(User):
    phone = models.CharField(max_length=15, default="+996")
    photo = models.ImageField(upload_to='users/')
    city = models.CharField(max_length=50)
    bio = models.TextField(max_length=500)
    github_url = models.URLField(max_length=200)
    portfolio_file = models.FileField(upload_to='portfolios/')
    experience_years = models.CharField(default=0)
    motivation_letter = models.TextField(max_length=1000)
    expectations = models.TextField(max_length=300)

    SCHEDULE_CHOICES = [
        ('OFFICE', 'OFFICE'),
        ('FLEX','FLEX'),
        ('REMOTE', 'REMOTE'),
    ]
    schedule = models.CharField(max_length=20, choices=SCHEDULE_CHOICES, default='OFFICE')
    
    GENDER_CHOICES = [
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE')
    ]
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)



    def __str__(self):
        return self.username
    


class Location(models.Model):
   name = models.CharField(max_length=50)

   def __str__(self):
        return self.name
   


class HouseTour(models.Model):
    title = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.location.name}'




class TourRegistration(models.Model):
    user = models.OneToOneField(DevUser, on_delete=models.CASCADE)
    joined_data = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username