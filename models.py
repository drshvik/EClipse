from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='profilepics',default='/profilepics/Screenshot_2023-11-07_104507_OV0cBvF.jpg')
    bio =models.CharField(max_length = 100)

    def __str__(self):
        return self.user.username + "'s Profile"
    

