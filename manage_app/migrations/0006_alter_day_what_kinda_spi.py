# Generated by Django 5.1 on 2024-10-03 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_app', '0005_day_file_upload_alter_day_detail_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='what_kinda_spi',
            field=models.CharField(choices=[('SPI3', 'SPI3'), ('ENG', 'ENG'), ('TAMATEBAKO', '玉手箱'), ('GAB', 'GAB'), ('CAB', 'CAB'), ('TG_WEB', 'TG-WEB'), ('OTHER', 'その他')], max_length=100, verbose_name='適性検査種類'),
        ),
    ]
