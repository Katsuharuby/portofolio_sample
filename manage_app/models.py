from django.db import models
from django.utils import timezone

class Day(models.Model):
    date_of_interview = models.DateTimeField('面談日付')
    name_of_company = models.CharField('会社名',max_length=200)
    what_kinda_spi = models.TextField('適性検査種類')
    date_of_spi = models.DateTimeField('適性検査日付')
    resume_of_spi = models.DateTimeField('履歴書提出日時')
    detail_text = models.TextField('詳細')


