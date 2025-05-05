from django.shortcuts import render

def index(request):
    return render(request, 'students/index.html')

def about_us(request):
    return render(request, 'students/about.html')

def service(request):
    return render(request, 'students/service.html')

def contact(request):
    return render(request, 'students/contact.html')