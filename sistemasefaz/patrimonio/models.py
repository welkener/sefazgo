from django.db import models
from taggit.managers import TaggableManager


class Setor(models.Model):
    descricao = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Setor"
        verbose_name_plural = "Setores"

    def __unicode__(self):
        s = u'%s' % (self.descricao)
        return s

    def __str__(self):
        s = u'%s' % (self.descricao)
        return s

class Patrimonio(models.Model):

    CHOICE_TIPO = (
        ('Mobiliario', 'Mobiliario'),
        ('Informatica', 'Informatica'),
        ('outros', 'Outros'),
    )

    CHOICE_STATUS = (
        ('Ativo', 'Ativo'),
        ('Baixado', 'Baixado'),
    )
    
    descricao = models.CharField(max_length=255)
    status = models.CharField(u'Status', max_length=15, choices=CHOICE_STATUS)
    nota_fiscal = models.IntegerField()
    plaqueta = models.IntegerField()
    numero_matricula = models.IntegerField()
    tipo = models.CharField(u'Tipo do Bem', max_length=15, choices=CHOICE_TIPO)
    data_aquisicao = models.DateTimeField(u'Data de Aquisição', auto_now=True, blank=True)
    data_baixa = models.DateTimeField(u'Data de Aquisição', auto_now=True, blank=True)
  
    setor = models.ForeignKey(
        Setor, related_name="setor", on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Patrimonio"
        verbose_name_plural = "Patrimonios"

    

    def __str__(self):
        return self.descricao
