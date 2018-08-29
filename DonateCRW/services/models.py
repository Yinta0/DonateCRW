from django.db import models
from django.utils.timezone import now

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date of created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Date of edition")

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ['-created']

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    subtitle = models.CharField(max_length=200, verbose_name="Subtitle")
    published = models.DateTimeField(verbose_name="Published", default=now)
    wallet_shop = models.CharField(max_length=100, verbose_name="Address Shop")
    crw_donate = models.IntegerField(verbose_name="Crown needed")
    wallet_donate = models.CharField(null=True, blank=True, max_length=100, verbose_name="Address for donate ")
    amount_donate = models.CharField(null=True, blank=True, max_length=18, verbose_name="Amount donate")
    amount_needed = models.CharField(null=True, blank=True, max_length=18, verbose_name="Amount needed")
    content = models.TextField(verbose_name="Description")
    image = models.ImageField(verbose_name="Image", upload_to="services")
    categories = models.ManyToManyField(Category, verbose_name="Categories", related_name="get_services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date of created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Date of edition")
    completed = models.BooleanField(default=False, verbose_name="Completed")

    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"
        ordering = ['-created']

    def __str__(self):
        return self.title

