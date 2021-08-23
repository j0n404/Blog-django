from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Article, Category

# Create your views here.

def lista_articulos(request):
    #Sacar todos los articulos
    articles = Article.objects.all()

    #Paginar los articulos
    paginator = Paginator(articles,3)

    #Recoger numero de página
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request, 'articles/listado_articulos.html', {
        'title':'Articulos disponibles',
        'articles':page_articles
    })

def category(request, category_id):
    category = Category.objects.get(id=category_id)

    articles = Article.objects.filter(categories = category_id)
    return render(request, 'categories/category.html', {
        'category':category,
        'articles':articles,
    })

def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'categories/all_categories.html',{
        'all_categories':categories,
    })

def article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request,'articles/detail.html', {
        'article':article,
    })