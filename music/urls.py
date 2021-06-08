from collections import namedtuple
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "music"

urlpatterns = [
    path('dashboard/', views.dashboard, name = "dashboard"),
    path('addmusic/',views.addmusic,name = "addmusic"),
    path('music/<int:id>',views.detail,name = "detail"),
    path('delete/<int:id>',views.delete,name = "delete"),
    path('',views.musics,name = "musics"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)