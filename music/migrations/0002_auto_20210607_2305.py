# Generated by Django 3.1.6 on 2021-06-07 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='content',
        ),
        migrations.RemoveField(
            model_name='music',
            name='note_image',
        ),
        migrations.RemoveField(
            model_name='music',
            name='source',
        ),
        migrations.RemoveField(
            model_name='music',
            name='title',
        ),
        migrations.AddField(
            model_name='music',
            name='composer',
            field=models.CharField(max_length=100, null=True, verbose_name='Sanatci'),
        ),
        migrations.AddField(
            model_name='music',
            name='piece',
            field=models.CharField(max_length=60, null=True, verbose_name='Parca '),
        ),
    ]