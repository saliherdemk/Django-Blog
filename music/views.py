from django import http
from django.shortcuts import redirect, render,HttpResponse,reverse
from .forms import MusicForm
from django.contrib import messages
from .models import Music
from django.contrib.auth.decorators import login_required

# Create your views here.

def musics(request):
    keyword = request.GET.get("keyword")

    if keyword :
        musics = Music.objects.filter(piece__contains = keyword)
        return render(request,"musics.html",{"musics":musics})

    musics = Music.objects.all()
    musics_length = musics.__len__()

    return render(request,"musics.html",{"musics" : musics, "musics_length" : musics_length })

def index(request):
    return render(request,"index.html")


@login_required(login_url = "user:login")
def dashboard(request):
    musics = Music.objects.filter(publisher = request.user)
    context = {
        "musics" : musics
    }
    return render(request,"musicdashboard.html",context)


@login_required(login_url = "user:login")
def addmusic(request):
    form = MusicForm(request.POST or None , request.FILES or None)

    if form.is_valid():
        music = form.save(commit=False)
        music.publisher = request.user
        music.save()

        messages.success(request,"Eser Başarıyla Oluşturuldu.")
        return redirect("music:dashboard")

    return render(request,"addmusic.html",{"form" : form})

def detail(request,id):
    music = Music.objects.filter(id = id).first()

    return render(request,"musicdetail.html",{"music" : music })


@login_required(login_url = "user:login")
def delete(request,id):
    music = Music.objects.filter(id = id).first()
    if music.publisher != request.user:
        messages.error(request, "Bu esere yetkiniz yok veya böyle bir eser yok.")
        return redirect("music:dashboard")
    else :
        if music :
            music.delete()
            messages.success(request,"Eser Başarıyla Silindi")

            return redirect("music:dashboard")
        else :
            return render(request,"musicdetail.html",{"music " : music})

def life(request):
    return render(request,"life.html")
