from django.core.mail import send_mail
from django.db.models.signals import m2m_changed, post_delete, post_save, pre_save
from django.dispatch import receiver
from .models import *
from django.core.files import File


@receiver(m2m_changed, sender=Doctor.likes.through)
def doctor_like_changed(sender, instance, **kwargs):
    instance.likes_count = instance.likes.count()
    instance.save()


