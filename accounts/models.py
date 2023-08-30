from django.db import models
from django.contrib.auth.models import AbstractUser
# pip install django_resized 명령어로 실행
from django_resized import ResizedImageField

# Create your models here.
class User(AbstractUser):
    profile_image = ResizedImageField(
        size=[500,500],
        crop=['middle', 'center'],
        upload_to='profile/',
    )
    # post_set =