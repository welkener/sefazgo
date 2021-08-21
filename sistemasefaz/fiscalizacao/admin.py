from django.contrib import admin
from .models import Fiscal, Empresa, Telefone, Email,Notificacao
# Register your models here.


class FiscalAdmin(admin.ModelAdmin):
    fields = ['descricao']

class EmpresaAdmin(admin.ModelAdmin):
    pass

class NotificacaoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Fiscal, FiscalAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Notificacao, NotificacaoAdmin)