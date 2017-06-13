from django.db import models


class Group(models.Model):

    id = models.CharField(
        primary_key=True,
        max_length=191
    )


class Member(models.Model):

    id = models.CharField(
        primary_key=True,
        max_length=191
    )

    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )


class Agreement(models.Model):

    id = models.CharField(
        primary_key=True,
        max_length=191
    )

    member = models.OneToOneField(
        Member,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
