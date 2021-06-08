# Generated by Django 3.1.6 on 2021-06-08 14:38

from django.db import migrations, models
import music.models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_auto_20210608_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='audio',
            field=models.FileField(null=True, storage=music.models.OverwriteStorage(), upload_to='', verbose_name='Ses '),
        ),
        migrations.AlterField(
            model_name='music',
            name='picture',
            field=models.FileField(blank=True, null=True, storage=music.models.OverwriteStorage(), upload_to='', verbose_name='Fotoğraf'),
        ),
    ]