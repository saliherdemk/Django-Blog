from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

# Create your models here.

class OverwriteStorage(FileSystemStorage):
    '''
    Muda o comportamento padrão do Django e o faz sobrescrever arquivos de
    mesmo nome que foram carregados pelo usuário ao invés de renomeá-los.
    '''
    def get_available_name(self, name,max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

class Music(models.Model):
    publisher = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    piece = models.CharField(max_length=60,verbose_name= "Eser ",null=True)
    composer = models.CharField(max_length=100,verbose_name="Sanatci ",null=True)
    picture = models.FileField(verbose_name="Fotoğraf",null=True,blank=True,storage=OverwriteStorage())
    audio = models.FileField(verbose_name="Ses ",null=True,storage=OverwriteStorage())
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta :
        ordering = ['-created_date']

