from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class MyUser(AbstractUser):
    pass


M = "MALE"
F = "FEMALE"
O = "OTHER"
GENDER_CHOICES = ((M, "Male"), (F, "Female"), (O, "Other"))


class BackendUser(models.Model):
    """
    User Model for Backend User
    """

    email = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    date_of_birth = models.DateField(_("Date Of Birth"))
    gender = models.CharField(
        _("Gender"), max_length=7, choices=GENDER_CHOICES, default=M
    )
    address = models.TextField(_("Address"))
    is_admin = models.BooleanField(_("Is Admin"))

    def __str__(self):
        return (
            f"{self.first_name.capitalize} {self.last_name.capitalize} | {self.email}"
        )


# TODO: FrontUser and BackUser with user model
