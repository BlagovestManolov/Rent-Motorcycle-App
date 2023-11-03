from django.db import models


class Motorcycle(models.Model):
    name = models.CharField(
        'Motorcycle name',
        max_length=255,
        blank=False,
        null=False,
    )

    date_of_creation = models.DateField(
        auto_now_add=True,
        blank=True,
    )

    type = models.CharField(
        default='Motorcycle',
        max_length=11,
        editable=False,
        blank=True,
    )

    price_1_to_7_days = models.PositiveIntegerField(
        'Price 1 to 7 days rent',
        null=False,
        blank=False,
    )

    price_8_to_14_days = models.PositiveIntegerField(
        'Price 8 to 14 days rent',
        null=False,
        blank=False,
    )

    price_15_to_21_days = models.PositiveIntegerField(
        'Price 15 to 21 days rent',
        null=False,
        blank=False,
    )

    price_22_to_30_days = models.PositiveIntegerField(
        'Price 22 to 30 days rent',
        null=False,
        blank=False,
    )

    main_image = models.FileField(
        'Motorcycle main image',
        upload_to='motorcycle/main_images/',
    )

    def __str__(self):
        return self.name


class MotorcycleDeposit(models.Model):
    motorcycle = models.OneToOneField(
        Motorcycle,
        related_name='deposit',
        on_delete=models.CASCADE,
    )

    date_of_creation = models.DateField(
        auto_now_add=True,
        blank=False,
    )

    deposit = models.PositiveIntegerField(
        'Motorcycle deposit price',
    )


class MotorcycleImage(models.Model):
    motorcycle = models.ForeignKey(
        Motorcycle,
        related_name='images',
        on_delete=models.CASCADE,
    )

    date_of_creation = models.DateField(
        auto_now_add=True,
        blank=True,
    )

    image = models.FileField(
        upload_to='motorcycle/more_images/',
        null=False,
        blank=False,
    )

    # Auto generated number of images related to the
    # specific motorcycle
    generated_image_number = models.PositiveIntegerField(
        default=0,
        editable=False,
    )

    def save(self, *args, **kwargs):
        existing_img_count = MotorcycleImage.objects.filter(motorcycle=self.motorcycle).count()
        self.generated_image_number = existing_img_count + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.motorcycle.name} Image {self.generated_image_number}'