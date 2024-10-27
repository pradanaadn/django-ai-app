from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.core.files.storage import FileSystemStorage
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def cv_upload(request):
    if request.method == "POST" and request.FILES["uploaded_file"]:
        file_cv = request.FILES["uploaded_file"]
        fs = FileSystemStorage()
        filename = fs.save(file_cv.name, file_cv)
        filename = fs.url(filename)

        return render(request, "cv_upload.html", {"filename": filename})
    else:
        return render(request, "cv_upload.html")
