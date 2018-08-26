from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nombre")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    wallet_self = models.CharField(max_length=100, verbose_name="Wallet Usuario")
    wallet_shop = models.CharField(max_length=100, verbose_name="Wallet Tienda")
    crw_donate = models.IntegerField(verbose_name="Crown necesarios")
    wallet_donate = models.CharField(null=True, blank=True, max_length=100, verbose_name="Wallet para Donar")
    amount_donate = models.CharField(null=True, blank=True, max_length=18, verbose_name="Saldo donado")
    amount_needed = models.CharField(null=True, blank=True, max_length=18, verbose_name="Crowns necesarios")
    content = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ['-created']

    def __str__(self):
        return self.title