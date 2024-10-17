from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass
    # can add additional fields here

    def __str__(self):
        return self.username
