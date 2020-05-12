from django.shortcuts import render

def index(request):
    return render(request,'basic_app/index.html')
def photos(request):
    return render(request,'basic_app/photos.html')
def code(request):
    return render(request,'basic_app/code.html')
def downloads(request):
    return render(request,'basic_app/downloads.html')
def online(request):
    return render(request,'basic_app/online.html')
