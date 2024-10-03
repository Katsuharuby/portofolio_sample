from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Day(models.Model):

    SPI_CHOICES = [
        ('SPI3', 'SPI3'),
        ('ENG', 'ENG'),
        ('TAMATEBAKO', '玉手箱'),
        ('GAB', 'GAB'),
        ('CAB', 'CAB'),
        ('TG_WEB', 'TG-WEB'),
        ('OTHER', 'その他'),
    ]

    date_of_interview = models.DateTimeField('面談日付')
    name_of_company = models.CharField('会社名',max_length=200)
    what_kinda_spi = models.CharField('適性検査種類',max_length=100, choices=SPI_CHOICES)
    date_of_spi = models.DateTimeField('適性検査日付')
    resume_of_spi = models.DateTimeField('履歴書提出日時')
    detail_text = models.TextField('詳細', blank = True, null = True)
    file_upload = models.FileField(upload_to='uploads/',blank = True, null = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='投稿者')

    def __str__(self):
        return self.name_of_company


