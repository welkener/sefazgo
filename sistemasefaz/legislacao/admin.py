from django.contrib import admin

# Register your models here.
from .models import Lei, Orgao, Esfera

@admin.register(Orgao)
class SecretariaAdmin(admin.ModelAdmin):
    fields = ['descricao']



@admin.register(Lei)
class LeiAdmin(admin.ModelAdmin):
    list_display = ('tipo_lei', 'numero', 'titulo', 'ano','orgao','esfera','arquivo','tag_list')
    list_filter = ('ano', 'tipo_lei','esfera','orgao')
    search_fields = ('titulo', 'numero','orgao','esfera')
    list_per_page = 20

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


