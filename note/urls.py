from collections import namedtuple
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "note"

urlpatterns = [
    path('dashboard/', views.dashboard, name = "dashboard"),
    path('addnote/',views.addnote,name = "addnote"),
    path('note/<int:id>',views.detail,name = "detail"),
    path('noteupdate/<int:id>',views.update,name = "update"),
    path('delete/<int:id>',views.delete,name = "delete"),
    path('',views.notes,name = "notes"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)