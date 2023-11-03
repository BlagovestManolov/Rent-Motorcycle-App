from django.db import models


class AboutUs(models.Model):
    address = models.CharField(
        'Our address',
        max_length=255,
        null=False,
        blank=False,
    )

    phone = models.CharField(
        'Our phone number',
        max_length=30,
        null=False,
        blank=False,
    )

    email = models.EmailField(
        'Our email',
        null=False,
        blank=False,
    )

    website = models.CharField(
        'Our website',
        max_length=125,
        null=False,
        blank=False,
    )
