# Generated by Django 3.1.6 on 2021-06-07 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20210213_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.FileField(null=True, upload_to='', verbose_name='Görüntülenecek Tablo'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=55, verbose_name='Başlık '),
        ),
    ]
