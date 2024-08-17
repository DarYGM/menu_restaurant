from django.db import models

# Create your models here.
class Categorias(models.Model):
    nombre= models.CharField(max_length=100,null=False,blank=False)
    visibilidad=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.nombre
    
    def __unicode__(self):
        return self.nombre    
    

class Producto(models.Model):
    nombre= models.CharField(max_length=100,null=False,blank=False)
    imagen=models.ImageField('Imagen de Productos', upload_to='Productos/')
    descripcion=models.CharField(max_length=100,null=False,blank=False)
    categoria=models.ForeignKey(Categorias,on_delete=models.CASCADE)
    precio = models.FloatField()
    preciodescuento=models.FloatField(editable=False,null=True,blank=True)
    visibilidad=models.BooleanField(default=True)
    disponibilidad=models.BooleanField(default=True)
    descuento=models.IntegerField(null=True,blank=True,help_text="Porciento de descuento para este producto, ejemplo: 15%",default=0)
    created=models.DateField(auto_now_add=True)


    class Meta:
        managed = True
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def save(self, *args, **kwargs):
        
        if self.precio and self.descuento:
            self.preciodescuento = self.precio * (1 - (self.descuento / 100))
        else:
            self.preciodescuento = self.precio
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre
    
    def __unicode__(self):
        return self.nombre   