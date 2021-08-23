from django.urls import path
from . import views

urlpatterns = [
    path('articulos/', views.lista_articulos, name='lista_articulos'),
    path('categoria/<int:category_id>/', views.category, name='category'),
    path('categorias/', views.all_categories, name='categories'),
    path('articulo/<int:article_id>/',views.article, name='article')
]
