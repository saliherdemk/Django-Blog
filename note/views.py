from django import http
from django.shortcuts import redirect, render,HttpResponse,reverse
from .forms import NoteForm
from django.contrib import messages
from .models import Note
from django.contrib.auth.decorators import login_required

# Create your views here.

def notes(request):
    keyword = request.GET.get("keyword")

    if keyword :
        notes = Note.objects.filter(title__contains = keyword)
        return render(request,"notes.html",{"notes":notes})

    notes = Note.objects.all()

    return render(request,"notes.html",{"notes" : notes })

def index(request):
    return render(request,"index.html")


@login_required(login_url = "user:login")
def dashboard(request):
    notes = Note.objects.filter(publisher = request.user)
    context = {
        "notes" : notes
    }
    return render(request,"notedashboard.html",context)


@login_required(login_url = "user:login")
def addnote(request):
    form = NoteForm(request.POST or None , request.FILES or None)

    if form.is_valid():
        note = form.save(commit=False)
        note.publisher = request.user
        note.save()

        messages.success(request,"Not Başarıyla Oluşturuldu.")
        return redirect("note:dashboard")

    return render(request,"addnote.html",{"form" : form})

def detail(request,id):
    note = Note.objects.filter(id = id).first()

    return render(request,"notedetail.html",{"note" : note })

@login_required(login_url = "user:login")
def update(request,id):
    
    note = Note.objects.filter(id = id).first()
    if note.publisher != request.user: 
        messages.error(request, "Bu nota erişme yetkiniz yok veya böyle bir not yok.")
        return redirect("note:dashboard")
    else:
        form = NoteForm(request.POST or None,request.FILES or None,instance = note)
        if form.is_valid():
            note = form.save(commit=False)
            note.publisher = request.user
            note.save()

            messages.success(request,"Not Başarıyla Güncellendi.")
            return redirect("note:dashboard")
        return render(request,"noteupdate.html",{"form" : form,"note" : note})
    

@login_required(login_url = "user:login")
def delete(request,id):
    note = Note.objects.filter(id = id).first()
    if note.publisher != request.user: 
        messages.error(request, "Bu nota erişme yetkiniz yok veya böyle bir not yok.")
        return redirect("note:dashboard")
    else :
        if note :
            note.delete()
            messages.success(request,"Not Başarıyla Silindi")

            return redirect("note:dashboard")
        else :
            return render(request,"notedetail.html",{"note " : note})


