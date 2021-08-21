# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class JetBookmark(models.Model):
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    user = models.IntegerField()
    date_add = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jet_bookmark'


class JetPinnedapplication(models.Model):
    app_label = models.CharField(max_length=255)
    user = models.IntegerField()
    date_add = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jet_pinnedapplication'


class LegislacaoEsfera(models.Model):
    descricao = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'legislacao_esfera'


class LegislacaoLei(models.Model):
    numero = models.IntegerField()
    tipo_lei = models.CharField(max_length=15)
    ano = models.CharField(max_length=4)
    titulo = models.TextField()
    arquivo = models.CharField(max_length=100)
    publicacao = models.DateTimeField()
    esfera = models.CharField(max_length=15)
    secretaria = models.ForeignKey('LegislacaoSecretaria', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'legislacao_lei'


class LegislacaoNoticia(models.Model):
    titulo = models.CharField(max_length=128)
    conteudo = models.TextField()
    data_cria = models.DateTimeField(blank=True, null=True)
    data_pub = models.DateField(blank=True, null=True)
    publicado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'legislacao_noticia'


class LegislacaoSecretaria(models.Model):
    descricao = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'legislacao_secretaria'


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

    class Meta:
        managed = False
        db_table = 'pagamentos'


class TaggitTag(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'taggit_tag'


class TaggitTaggeditem(models.Model):
    object_id = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    tag = models.ForeignKey(TaggitTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'taggit_taggeditem'
        unique_together = (('content_type', 'object_id', 'tag'),)


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
