from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def prueba(request):
    return render(request, 'prueba.html')