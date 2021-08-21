from django.contrib import admin

# Register your models here.
from .models import Setor, Patrimonio

@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
    fields = ['descricao']



@admin.register(Patrimonio)
class PatrimonioAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'descricao', 'status', 'plaqueta', 'numero_matricula', 'setor')
    list_filter = ('tipo', 'status','descricao','setor', 'data_aquisicao', 'numero_matricula', 'plaqueta')
    search_fields = ('tipo', 'status','descricao','setor', 'data_aquisicao', 'numero_matricula', 'plaqueta')
    list_per_page = 20


