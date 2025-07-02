from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_sessions = models.IntegerField(default=0)
    total_energy_consumed = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_amount_spent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    
class Gallery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gallery_sessions')
    name = models.CharField(max_length=50)
    gallery_images = models.ImageField(upload_to='images/')
    gps_location = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    memories = models.CharField(max_length=256)
    date = models.DateField()

    def __str__(self):
        return self.name