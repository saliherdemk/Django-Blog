from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name="Yazar ")
    title = models.CharField(max_length = 55,verbose_name= "Başlık ")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add = True)
    article_image = models.FileField(null=True,verbose_name="Görüntülenecek Tablo")
    def __str__(self):
        return self.title

    class Meta :
        ordering = ['-created_date']


class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name="Makale",related_name="comment")
    comment_author = models.CharField(max_length=50,verbose_name="isim")
    comment_content = models.CharField(max_length=400,verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.comment_content

    class Meta :
        ordering = ['-comment_date']



