from django.contrib import admin
from .models import Producto,Categorias
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    #list_display = ("all")
    readonly_fields = ('preciodescuento',)
    def save_model(self, request, obj, form, change):
        obj.save()
        
admin.site.register(Categorias)
admin.site.register(Producto,ProductoAdmin)