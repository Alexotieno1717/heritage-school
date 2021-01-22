from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'heritage/index.html')

def about(request):
    return render(request, 'heritage/about.html')

def curriculum(request):
    return render(request, 'heritage/curriculum.html')

def news(request):
    return render(request, 'heritage/news.html')

def awwards(request):
    return render(request, 'heritage/awwards.html')

def give(request):
    return render(request, 'heritage/give.html')

def contact(request):
    return render(request, 'heritage/contact.html')