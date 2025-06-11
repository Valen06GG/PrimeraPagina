from django.shortcuts import render

def index(request):
    context = {"mensaje": "Bienvenidos a mi pagina Django"}
    return render(request, "MiPrimerPagina/index.html", context)
