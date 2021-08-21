from django.db import models

# Create your models here.


class Pagamentos(models.Model):
    nume_parc = models.CharField(max_length=255, blank=True, null=True)
    nume_titu = models.CharField(max_length=255, blank=True, null=True)
    codi_agen = models.CharField(max_length=255, blank=True, null=True)
    codi_aget = models.CharField(max_length=255, blank=True, null=True)
    sequ_bdam = models.CharField(max_length=255, blank=True, null=True)
    sequ_tpam = models.CharField(max_length=255, blank=True, null=True)
    sequ_dam = models.CharField(max_length=255, blank=True, null=True)
    codi_rece = models.CharField(max_length=255, blank=True, null=True)
    codi_tipo = models.CharField(max_length=255, blank=True, null=True)
    valo_impo = models.CharField(max_length=255, blank=True, null=True)
    base_calc = models.CharField(max_length=255, blank=True, null=True)
    valo_mult = models.CharField(max_length=255, blank=True, null=True)
    valo_juro = models.CharField(max_length=255, blank=True, null=True)
    valo_corr = models.CharField(max_length=255, blank=True, null=True)
    data_paga = models.CharField(max_length=255, blank=True, null=True)
    codi_tipa = models.CharField(max_length=255, blank=True, null=True)
    data_baix = models.CharField(max_length=255, blank=True, null=True)
    matr_usua = models.CharField(max_length=255, blank=True, null=True)
    peri_refe = models.CharField(max_length=255, blank=True, null=True)
    valo_tota = models.CharField(max_length=255, blank=True, null=True)

    
    def __unicode__(self):
        s = u'%s' % (self.nume_titu)
        return s

    def __str__(self):
        s = u'%s' % (self.nume_titu)
        return s

    class Meta:
        managed = False
        db_table = 'pagamentos'
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"


class Titulos(models.Model):
    nume_titu = models.CharField(max_length=255, blank=True, null=True)
    codi_cont = models.CharField(max_length=255, blank=True, null=True)
    codi_imov = models.CharField(max_length=255, blank=True, null=True)
    codi_pess = models.CharField(max_length=255, blank=True, null=True)
    nume_proc = models.CharField(max_length=255, blank=True, null=True)
    codi_unid = models.CharField(max_length=255, blank=True, null=True)
    codi_rece = models.CharField(max_length=255, blank=True, null=True)
    codi_situ = models.CharField(max_length=255, blank=True, null=True)
    codi_tipo = models.CharField(max_length=255, blank=True, null=True)
    nume_docu = models.CharField(max_length=255, blank=True, null=True)
    codi_moed = models.CharField(max_length=255, blank=True, null=True)
    valo_titu = models.CharField(max_length=255, blank=True, null=True)
    data_lanc = models.CharField(max_length=255, blank=True, null=True)
    peri_refe = models.CharField(max_length=255, blank=True, null=True)
    obse_situ = models.CharField(max_length=255, blank=True, null=True)
    flag_titu = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titulos'
        verbose_name = "Titulo"
        verbose_name_plural = "Titulos"

    def __unicode__(self):
        s = u'%s' % (self.nume_titu)
        return s

    def __str__(self):
        s = u'%s' % (self.nume_titu)
        return s
    