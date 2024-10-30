from django.urls import path

from . import views

urlpatterns = [
    path("", views.index , name="index"),
    path("upload", views.cv_upload , name="cv_upload")
    
]
