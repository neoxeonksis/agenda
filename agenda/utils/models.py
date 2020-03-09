#Django
from django.db import models


class CommonModel(models.Model):

    class Meta:
        abstract = True

