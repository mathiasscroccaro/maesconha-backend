from django.db import models


class BaseUser(models.Model):
    first_name = models.CharField(
        max_length=30,
        blank=False
    )
    last_name = models.CharField(
        max_length=100,
        blank=False
    )
    birth = models.DateField()
    patient = models.BooleanField(default=False)


class AssociatedUser(BaseUser):
    pass


class DependentUser(BaseUser):
    associated_user = models.ForeignKey(
        AssociatedUser, 
        on_delete=models.CASCADE,
        related_name='dependent_users'
    )

    def __init__(self):
        patient = True


class Document(models.Model):
   pass 
