from django.db import models


class IncludedInThePrice(models.Model):
    name = models.CharField(
        'Included article in the price',
        max_length=255,
        null=False,
        blank=False,
    )

    date_of_creation = models.DateField(
        auto_now_add=True,
        blank=True,
    )

    image = models.FileField(
        upload_to='included_in_the_price/',
    )

    def __str__(self):
        return self.name
