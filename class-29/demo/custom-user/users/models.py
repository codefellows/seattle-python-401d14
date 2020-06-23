from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):

    # unique_together
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
