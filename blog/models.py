from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.CharField(max_length=155, verbose_name='Descripción')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo')
    description  = models.TextField(max_length=300, verbose_name='Descripción',default='descrip')
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(default='null', blank=True, verbose_name='Imagen', upload_to='articles')
    public = models.BooleanField(verbose_name='Publicado')

    #relación 1 a 1, un articulo es echo por 1 usuario
    user = models.ForeignKey(User, editable=False, verbose_name ='Usuario', on_delete=models.CASCADE)

    #Relacion de 1 a muchos, 1 articulo puede tener muchas categorías.
    categories = models.ManyToManyField(Category, verbose_name = 'Categorías', blank= True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado el')

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"

    def __str__(self):
        return self.title


