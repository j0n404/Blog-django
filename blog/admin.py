from django.contrib import admin
from .models import Article, Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', )
    list_display= ('name', 'created_at')
    search_fields= ('name', 'description')

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'updated_at','user')
    search_fields = ('title', 'content', 'user__username', 'categories__name')
    list_display= ('title', 'user', 'created_at', 'public')
    list_filter = ('public', 'user__username', 'categories__name',)
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()
                                                                                

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)