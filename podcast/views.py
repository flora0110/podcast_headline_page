from django.shortcuts import render
from django.http import HttpResponse
from . import podcast_to_headline


def index(request):
    return HttpResponse("Hello, Django .")


def uploadShow(request):
    str = ""
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]
        str = uploadedFile.read().decode('utf-8')
        # print(str)
        #print(uploadedFile.read().decode('utf-8'))
        #print(uploadedFile.read())
        #print(type(uploadedFile.read()))

    return render(request, "podcast/upload_show.html", context={
        "file_context": podcast_to_headline.split(str),
    })
