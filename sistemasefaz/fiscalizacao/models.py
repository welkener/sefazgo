from django.db import models

# Create your models here.
TIPO_TELEFONE = [
    ('FIX', "Fixo"),
    ('CEL', "Celular"),
    ('FAX', "Fax"),
    ('OUT', "Outro"),
]

TIPO_ENDERECO = [
    ('UNI', 'Único'),
    ('RES', 'Residencial'),
    ('COM', 'Comercial'),
    ('COB', 'Cobrança'),
    ('ENT', 'Entrega'),
    ('OUT', 'Outro'),
]

TIPO_PROCESSAMENTO = [
    ('Aberto', 'Aberto'),
    ('Recebido', 'Recebido'),
    ('Processado', 'Processado'),
]

UF_SIGLA = [
    ('AC', 'AC'),
    ('AL', 'AL'),
    ('AP', 'AP'),
    ('AM', 'AM'),
    ('BA', 'BA'),
    ('CE', 'CE'),
    ('DF', 'DF'),
    ('ES', 'ES'),
    ('EX', 'EX'),
    ('GO', 'GO'),
    ('MA', 'MA'),
    ('MT', 'MT'),
    ('MS', 'MS'),
    ('MG', 'MG'),
    ('PA', 'PA'),
    ('PB', 'PB'),
    ('PR', 'PR'),
    ('PE', 'PE'),
    ('PI', 'PI'),
    ('RJ', 'RJ'),
    ('RN', 'RN'),
    ('RS', 'RS'),
    ('RO', 'RO'),
    ('RR', 'RR'),
    ('SC', 'SC'),
    ('SP', 'SP'),
    ('SE', 'SE'),
    ('TO', 'TO'),
]

class Fiscal(models.Model):
    descricao = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Fiscal"
        verbose_name_plural = "Fiscais"

    def __unicode__(self):
        s = u'%s' % (self.descricao)
        return s

    def __str__(self):
        s = u'%s' % (self.descricao)
        return s

class Empresa(models.Model):
    # Dados
    nome_razao_social = models.CharField(max_length=255)
    inscricao_municipal = models.CharField(
        max_length=32, null=True, blank=True)
    informacoes_adicionais = models.CharField(
        max_length=1055, null=True, blank=True)
    cnpj = models.CharField(max_length=32, null=True, blank=True)
    nome_fantasia = models.CharField(max_length=255, null=True, blank=True)
    inscricao_estadual = models.CharField(max_length=32, null=True, blank=True)
    # Dados padrao
    tipo_endereco = models.CharField(
        max_length=3, null=True, blank=True, choices=TIPO_ENDERECO)
    logradouro = models.CharField(max_length=255, null=True, blank=True)
    numero = models.CharField(max_length=16, null=True, blank=True)
    bairro = models.CharField(max_length=64, null=True, blank=True)
    complemento = models.CharField(max_length=64, null=True, blank=True)
    pais = models.CharField(max_length=32, null=True,
                            blank=True, default='Brasil')
    municipio = models.CharField(max_length=64, null=True, blank=True)
    cep = models.CharField(max_length=16, null=True, blank=True)
    uf = models.CharField(max_length=3, null=True,
                          blank=True, choices=UF_SIGLA)



    @property
    def format_cnpj(self):
        if self.cnpj:
            return 'CNPJ: {}'.format(self.cnpj)
        else:
            return ''

    @property
    def format_ie(self):
        if self.inscricao_estadual:
            return 'IE: {}'.format(self.inscricao_estadual)
        else:
            return ''

    def __unicode__(self):
        s = u'%s' % (self.nome_razao_social)
        return s

    def __str__(self):
        s = u'%s' % (self.nome_razao_social)
        return s

class Telefone(models.Model):
    empresa = models.ForeignKey(
        Empresa, related_name="telefone", on_delete=models.CASCADE)
    tipo_telefone = models.CharField(
        max_length=8, choices=TIPO_TELEFONE, null=True, blank=True)
    telefone = models.CharField(max_length=32)

    def get_telefone_apenas_digitos(self):
        return self.telefone.replace('(', '').replace(' ', '').replace(')', '').replace('-', '')


class Email(models.Model):
    empresa = models.ForeignKey(
        Empresa, related_name="email", on_delete=models.CASCADE)
    email = models.CharField(max_length=255)

class Notificacao(models.Model):
    empresa = models.ForeignKey(
        Empresa, related_name="notificacao", on_delete=models.CASCADE)
    numeroAuto = models.CharField(max_length=255)
    data = models.DateField
    arquivo = models.FileField(upload_to='uploads/')
    status = models.CharField(max_length=20, null=True,
                          blank=True, choices=TIPO_PROCESSAMENTO)

    def __unicode__(self):
        s = u'%s' % (self.empresa.nome_razao_social)
        return s

    def __str__(self):
        s = u'%s' % (self.empresa.nome_razao_social)
        return s