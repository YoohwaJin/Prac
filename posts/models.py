from django.db import models
from django_resized import ResizedImageField
# Create your models here.
class Post(models.Model):
    context = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ResizedImageField(
        size=[500, 500],
        crop=['middle', 'center'],
        upload_to='image/%Y/%m'
    )