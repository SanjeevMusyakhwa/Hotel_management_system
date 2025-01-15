from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuid.django_fields import ShortUUIDField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Choices
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

PROVINCE_CHOICES = (
    ('Province 1', 'Province 1'),
    ('Province 2', 'Province 2'),
    ('Province 3', 'Province 3'),
    ('Province 4', 'Province 4'),
    ('Province 5', 'Province 5'),
    ('Province 6', 'Province 6'),
    ('Province 7', 'Province 7'),
    ('None', 'None'),
)

IDENTITY_CHOICES = (
    ('Citizenship', 'Citizenship'),
    ('NID', 'NID'),
    ('Driving License', 'Driving License'),
    ('Passport', 'Passport'),
    ('None', 'None'),
)

def user_directory_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{instance.id}.{ext}"
    return f"user_{instance.id}/{filename}"

class User(AbstractUser):
    full_name = models.CharField(max_length=200, verbose_name='Full Name')
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')

    otp = models.CharField(max_length=6, null=True, blank=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username', 'email', 'full_name']

    def __str__(self):
        return f"{self.full_name} ({self.username}) - {self.phone_number}"

class Profile(models.Model):
    pid = ShortUUIDField(length=6, max_length=15, alphabet="abcdefghijklmnopqrst1234567890")
    image = models.FileField(upload_to=user_directory_path, default="defaults/image.jpg", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=200)
    province = models.CharField(max_length=20, choices=PROVINCE_CHOICES, default='None')
    identity_type = models.CharField(max_length=20, choices=IDENTITY_CHOICES, null=True, blank=True, default='None')
    identity_img = models.FileField(upload_to=user_directory_path, default="defaults/identity.jpg", null=True, blank=True)
    wallet = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    verified = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.user.full_name or self.user.username} - {self.user.phone_number}"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
