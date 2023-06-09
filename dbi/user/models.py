from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class User(models.Model):
    user_name   = models.CharField(max_length=20, unique=True, null=False, blank=False)
    email       = models.EmailField()
    password    = models.CharField(max_length=50, null=False, blank=False)
    age         = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)], null=False, blank=False)
    date_joined = models.DateField(auto_now_add=True)

