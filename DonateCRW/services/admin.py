from django.contrib import admin
from .models import Service, Category

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated','wallet_donate', 'completed')

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)