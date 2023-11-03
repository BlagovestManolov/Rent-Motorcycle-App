from django.db import models


class DepositAndInsurance(models.Model):
    question = models.CharField(
        'Question',
        max_length=300,
        null=False,
        blank=False,
    )

    date_of_creation = models.DateField(
        auto_now_add=True,
        blank=True,
    )

    answer = models.TextField(
        'Answer',
        blank=False,
        null=False,
    )


class Condition(models.Model):
    question = models.CharField(
        'Question',
        max_length=300,
        null=False,
        blank=False,
    )

    date_of_creation = models.DateField(
        auto_now_add=True,
        blank=True,
    )

    answer = models.TextField(
        'Answer',
        blank=False,
        null=False,
    )