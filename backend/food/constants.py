from django.db import models
from django.utils.translation import gettext_lazy as _


class Units(models.TextChoices):
    GRAM = "g", _("Gram")
    Milliliter = "mL", _("Milliliter")
