from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Note(models.Model):
    publisher = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    title = models.CharField(max_length=60,verbose_name= "Başlık ")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    note_image = models.FileField(blank=True,null=True,verbose_name="Notunuza Fotoraf Ekleyin")
    source = RichTextField()
    def __str__(self):
        return self.title
    class Meta :
        ordering = ['-created_date']

