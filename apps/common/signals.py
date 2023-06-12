from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.accounts.models import User,CustomToken

@receiver(post_save, sender=User)
def create_custom_token(sender, instance, created, **kwargs):
    print("================== create_custom_token ===================",instance)
    if created:
        token = CustomToken(user=instance)
        token.generate_token()
        token.save()
        
