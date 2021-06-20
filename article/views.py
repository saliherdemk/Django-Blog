from django import http
from django.shortcuts import redirect, render,HttpResponse,reverse
from .forms import ArticleForm
from django.contrib import messages
from .models import Article,Comment
from django.contrib.auth.decorators import login_required

# Create your views here.

def articles(request):
    keyword = request.GET.get("keyword")

    if keyword :
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})

    articles = Article.objects.all()
    articles_length = articles.__len__()

    return render(request,"articles.html",{"articles" : articles, "articles_length" : articles_length })

def index(request):
    return render(request,"index.html")

@login_required(login_url = "user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles" : articles
    }
    return render(request,"dashboard.html",context)

@login_required(login_url = "user:login")
def addarticle(request):
    form = ArticleForm(request.POST or None , request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request,"Tablo Başarıyla Oluşturuldu.")
        return redirect("article:dashboard")

    return render(request,"addarticle.html",{"form" : form})

def detail(request,id):
    article = Article.objects.filter(id = id).first()

    comments = article.comment.all()


    return render(request,"detail.html",{"article" : article ,"comment" : comments})

@login_required(login_url = "user:login")
def update(request,id):
    
    article = Article.objects.filter(id = id).first()
    if article.author != request.user: 
        messages.error(request, "Bu tabloya erişme yetkiniz yok veya böyle bir tablo yok.")
        return redirect("article:dashboard")
    else:
        form = ArticleForm(request.POST or None,request.FILES or None,instance = article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()

            messages.success(request,"Tablo Başarıyla Güncellendi.")
            return redirect("article:dashboard")
        return render(request,"update.html",{"form" : form,"article" : article})
    

@login_required(login_url = "user:login")
def delete(request,id):
    article = Article.objects.filter(id = id).first()
    if article.author != request.user: 
        messages.error(request, "Bu tabloya erişme yetkiniz yok veya böyle bir tablo yok.")
        return redirect("article:dashboard")
    else :
        if article :
            article.delete()
            messages.success(request,"Tablo Başarıyla Silindi")

            return redirect("article:dashboard")
        else :
            return render(request,"detail.html",{"article" : article})


def comment(request,id):
    article = Article.objects.filter(id = id).first()

    if article :
        if request.method == "POST" :
            comment_author = request.POST.get("comment_author")
            comment_content = request.POST.get("comment_content")

            newComment = Comment(comment_author = comment_author,comment_content = comment_content)

            newComment.article = article

            newComment.save()
        return redirect(reverse("article:detail",kwargs = {"id" : id}))
    else :
        return render(request,"detail.html",{"article" : article})


