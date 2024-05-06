from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.urls import reverse


class Web_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='web_user')
    photo = models.ImageField(upload_to='account_photo', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.user.first_name


class Doctor(models.Model):
    CATEGORY_CHOICES = (
        ('پزشک عمومی', 'پزشک عمومی'),
        ('متخصص زیبایی', 'متخصص زیبایی'),
        ('متخصص قلب', 'متخصص قلب'),
        ('متخصص غدد', 'متخصص غدد'),
        ('متخصص زنان', 'متخصص زنان'),
        ('متخصص داخلی', 'متخصص داخلی'),
        ('متخصص گوش،حلق،بینی', 'متخصص گوش،حلق،بینی'),
        ('متخصص داخلی', 'متخصص داخلی'),
        ('جراخ پلاستیک', 'جراخ پلاستیک'),
        ('متخصص اطفال', 'متخصص اطفال'),
        ('متخصص مامایی', 'متخصص مامایی'),
        ('متخصص مغز و اعصاب', 'متخصص مغز و اعصاب'),
        ('دندانپزشک', 'دندانپزشک'),

    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor')
    photo = models.ImageField(upload_to='account_photo')
    description = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    mc_number = models.CharField(max_length=20)
    expert = models.CharField(choices=CATEGORY_CHOICES, max_length=120)
    likes = models.ManyToManyField(User, related_name='doctor_likes', blank=True)
    likes_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.first_name

    def get_absolute_url(self):
        return reverse("doc_ja_app:doctor_detail", args=[self.id])


class Reservation(models.Model):
    # day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='reservations')
    day = models.CharField(max_length=40)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='reservations')
    web_user = models.ForeignKey(Web_user, on_delete=models.CASCADE, related_name='reservations')
    # hour = models.OneToOneField(Hour, on_delete=models.CASCADE, related_name='reservation')
    hour = models.PositiveIntegerField(default=0)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.web_user} + {self.doctor} + {self.day} + {self.hour}'


class Doctor_C(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_comments')
    user = models.ForeignKey(Web_user, on_delete=models.CASCADE, related_name='doctor_comment_owner')
    name = models.CharField(max_length=20, blank=True)
    message = models.TextField(verbose_name='کامنت')
    email = models.CharField(max_length=30, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]

    def __str__(self):
        return f"{self.user} : {self.doctor}"
