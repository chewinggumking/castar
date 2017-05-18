from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
# from .models import StarPhotos

def mobile_val(mobile):
    digit_list = []
    for digit in range(0,10):
        digit_list.append(str(digit))
    if mobile is not None:
        if len(mobile) != 10:
            raise ValidationError(
            ("Mobile Number has less than 10 digits"),
            params = {'mobile':mobile}
            )
        for number in mobile:
            if number not in digit_list:
                raise ValidationError(
                ("Only numbers allowed in Mobile Number"),
                params = {'mobile':mobile}
                )
#Validator to check photos do not exceed 20 photos per user
def photo_nums(file):
    total_pics = total.photos.count()
    if total_pics == 20:
        raise ValidationError(
        ("You have reached the maximum limit of photo uploads for your account"),
        params = {"total_pics":total_pics}
        )
