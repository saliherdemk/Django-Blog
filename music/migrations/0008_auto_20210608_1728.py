# Generated by Django 3.1.6 on 2021-06-08 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20210608_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='audio',
            field=models.FileField(null=True, upload_to='', verbose_name='Ses '),
        ),
        migrations.AlterField(
            model_name='music',
            name='composer',
            field=models.CharField(max_length=100, null=True, verbose_name='Sanatci '),
        ),
    ]
