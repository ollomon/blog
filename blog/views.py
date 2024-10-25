from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "blog/inicio.html")

def post(request):
    return render(request, 'blog/detalle.html')

