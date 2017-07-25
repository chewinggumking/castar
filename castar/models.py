from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.base import ModelBase
from dateutil.relativedelta import relativedelta
from datetime import date
# Importing a mobile validator for mobile number field to check if it match Indian Mobile numbers
from .validators import mobile_val

# Create your models here.


class StarProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Date of Birth: ")
    address_1 = models.CharField(max_length=200, blank=True, help_text="Please enter your buildin name and flat number.", verbose_name="Building\\Flat Number")
    address_2 = models.CharField(max_length=200, blank=True, help_text="Please enter your street name and\\or locality", verbose_name="Street\\Locality")
    address_3 = models.CharField(max_length=200, blank=True, help_text="Please enter the area you live in.", verbose_name="Area Name")
    address_4 = models.CharField(max_length=200, blank=True, help_text="Please enter the city you live in.", verbose_name="City")
    address_5 = models.CharField(max_length=200, blank=True, help_text="Please enter the state you live in.", verbose_name="State")
    address_6 = models.CharField(max_length=6, blank=True, help_text="Please enter your pin code.", verbose_name="Pin Code")
    mobile_number = models.CharField(max_length=10, blank=True, help_text="Please enter your mobile number without the country code.",
    validators =[mobile_val] ,verbose_name= "Mobile Number +91")
    date_joined = models.DateField(auto_now_add=True)
    # Choice for gender selection
    GENDER_CHOICES = (
    ('F', "Female"),
    ('M', "Male"),
    ('O', "Other"),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default ='F')

    def starage(self):
        today = date.today()
        age = relativedelta(today, self.date_of_birth)
        return str(age.years)
    age = property(starage)

    def mobile(self):
        return "+91 {0}".format(self.mobile_number)


    def __str__(self):
        return "Name: {0} Age: {1} Gender {2}".format(self.user, self.age, self.gender)




class StarPhotos(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    PHOTO_CATEGORY = (
    ('HS', "Head Shot"),
    ('WP', "Western Party Wear"),
    ('IP', "Indian Party Wear"),
    ('SW', "Swim Wear"),
    ('CW', "Casual Wear"),
    )
    category = models.CharField(max_length=2, choices=PHOTO_CATEGORY, default='CW')
    # This FileField should preferaby be changed to ImageField with pillow installed.
    photos = models.FileField(max_length=200, upload_to='images/',)

    def __str__(self):
        return "Images for {0}".format(self.user)


    # def clean(self,):
    #     # checkUser = self.cleaned_data()
    #     # print (checkUser)
    #     photo_count(self)


    class Meta:
        verbose_name_plural = "Star Photos"
