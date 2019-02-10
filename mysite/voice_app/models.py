from django.db import models
from django.core.validators import FileExtensionValidator

class VoiceActor(models.Model):
    """
    声優個人を管理する
    """
    
    SEX_CHOICES = (
        (1, '男性'),
        (2, '女性'),
    )

    name               = models.CharField('声優名', max_length=50)
    age                = models.IntegerField('年齢', null=True, blank=True) 
    sex                = models.IntegerField('性別', choices=SEX_CHOICES)
    birthday           = models.CharField('誕生日', max_length=30, null=True, blank=True)
    office             = models.CharField('事務所', max_length=100, null=True, blank=True)
    office_URL         = models.URLField('事務所URL', null=True, blank=True)
    official_site_name = models.CharField('個別サイト', max_length=100, null=True,blank=True)
    offisal_site_URL   = models.URLField('個別サイトURL', null=True, blank=True)
    image              = models.ImageField('画像', null=True, blank=True)
    masterpiece        = models.TextField('代表作品', null=True, blank=True)

    class Meta:
        db_table = 'voice_actor'

    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name


class Property(models.Model):
    """
    属性名を管理する
    """

    property_name = models.CharField('属性名', max_length=100)

    class Meta:
        db_table = 'property'
        unique_together = ('property_name', )

    def __str__(self):
        return self.property_name

class SampleVoice(models.Model):
    """
    音声データを管理する
    """

    voice_actor    = models.ForeignKey(VoiceActor, verbose_name='声優名', on_delete=models.CASCADE)
    words          = models.TextField('台詞')
    voice          = models.FileField(verbose_name='音声データ', validators=[FileExtensionValidator(['mp3', 'wav'])])
    property_name  = models.ManyToManyField(Property)
    title          = models.CharField('作品名', max_length=100)
    character_name = models.CharField('キャラクタ名', max_length=100)

    class Meta:
        db_table = 'sample_voice'

    def __str__(self):
        return f'{str(self.voice_actor)} - {self.words}'

