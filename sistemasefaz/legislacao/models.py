from django.db import models
from taggit.managers import TaggableManager


class Orgao(models.Model):
    descricao = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Orgão"
        verbose_name_plural = "Orgãos"

    def __unicode__(self):
        s = u'%s' % (self.descricao)
        return s

    def __str__(self):
        s = u'%s' % (self.descricao)
        return s

class Esfera(models.Model):
    descricao = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Esfera"
        verbose_name_plural = "Esferas"

    def __unicode__(self):
        s = u'%s' % (self.descricao)
        return s

    def __str__(self):
        s = u'%s' % (self.descricao)
        return s

class Lei(models.Model):

    CHOICE_TIPO_LEI = (
        ('complementar', 'Lei complementar'),
        ('ordinaria', 'Lei ordinária'),
        ('decreto', 'Decreto'),
        ('portaria', 'Portaria'),
        ('convenio', 'Convênios Municipais'),
        ('instrucao', 'Instruções Normativas'),
        ('outros', 'Outros'),
    )

    CHOICE_ESFERA = (
        ('Federal', 'Federal'),
        ('Estadual', 'Estadual'),
        ('Municipal', 'Municipal'),
    )

    numero = models.IntegerField()
    tipo_lei = models.CharField(u'Tipo do documento', max_length=15, choices=CHOICE_TIPO_LEI)
    ano = models.CharField(max_length=4)
    titulo = models.TextField()
    arquivo = models.FileField()
    publicacao = models.DateTimeField(u'publicação', auto_now=True, blank=True)
    tags = TaggableManager()

    orgao = models.ForeignKey(
        Orgao, related_name="lei", on_delete=models.CASCADE)

    esfera =  models.CharField(u'Esfera', max_length=15, choices=CHOICE_ESFERA)




    class Meta:
        verbose_name = "Legislação"
        verbose_name_plural = "Legislações"

    def chage_view(self):
        return self.arquivo

    def __str__(self):
        return self.titulo

        