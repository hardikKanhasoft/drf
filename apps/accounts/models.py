


from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from apps.common.models import TimeStampModel
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.utils.crypto import get_random_string

phone_reguler_expression = RegexValidator(
    regex=r"^\+?1?\d{9,15}$",
    message="The phone number must be entered in the following format: ‘+999999999’. Up to 15 digits are allowed.",
)

class User(AbstractUser, TimeStampModel):
    # Custom User Model 
    last_name = models.CharField(_("last_name"), max_length=100, blank=True, null=True)
    first_name = models.CharField(_("first_name"), max_length=100, blank=True, null=True)
    username = models.CharField(_("username"), max_length=100, blank=True, null=True)
    email = models.EmailField(_("email address"), unique=True)
    birth_date = models.DateField(_("date of birth"), blank=True, null=True)
    address = models.TextField(_("address"), blank=True, null=True)
    phone_number = models.CharField(_("phone number"), validators=[phone_reguler_expression], max_length=17, blank=True)
    avatar = models.ImageField(
        upload_to="userimages",
        max_length=254,
        blank=True,
        null=True,
        default="default.jpg",
    )
    is_verified = models.BooleanField(_("user is verified or not"), default=False)
    groups = models.ManyToManyField(Group, verbose_name=_("groups"), blank=True, related_name="user_groups")
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("user permissions"),
        blank=True,
        related_name="user_permissions_set",
    )
    
class CustomToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=40, unique=True)
    
    def generate_token(self):
        print("==================== generate_token ===============")
        self.token = get_random_string(40) 