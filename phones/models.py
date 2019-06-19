from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    image = models.ImageField()
    release_date = models.DateField(null=True)
    lte_exists = models.BooleanField()
    slug = models.SlugField()

