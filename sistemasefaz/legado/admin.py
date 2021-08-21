from django.contrib import admin
from .models import Pagamentos, Titulos
# Register your models here.

#@admin.register(Pagamentos)
class PagamentosAdmin(admin.ModelAdmin):
    list_display = ('nume_titu', 'codi_rece', 'valo_impo', 'base_calc','data_paga','valo_tota')
    #list_filter = ('nume_titu', )
    search_fields = ('nume_titu', 'codi_rece','valo_impo','base_calc','data_paga','valo_tota')
    list_per_page = 5
    #pass

#@admin.register(Titulos)
class TitulosAdmin(admin.ModelAdmin):
    list_display = ('nume_titu', 'codi_imov', 'codi_pess', 'codi_rece','valo_titu','obse_situ','data_lanc','peri_refe')
    #list_filter = ('nume_titu', )
    search_fields = ('nume_titu', 'codi_imov','codi_pess','codi_rece','valo_titu')
    list_per_page = 5
    #pass

admin.site.register(Pagamentos, PagamentosAdmin)
admin.site.register(Titulos, TitulosAdmin)
