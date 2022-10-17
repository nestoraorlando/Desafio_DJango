from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "ejemplo/saludar.html", {"nombre":"Néstor","apellido":"Orlando"})

def index_dos(request, nombre, apellido):
    return render(request, "ejemplo/saludar.html", {"nombre":nombre,"apellido":apellido})

def index_tres(request):

    return render(request, "ejemplo/saludar.html",
    {"notas":[1,2,3,4,5,6,7,8,9]}
    )


def i_m_corporal(request, peso, altura):
    imc = int(peso) / (int(altura)/100) ** (int(altura)/100)
    return render(request, "ejemplo/imc.html", {"imc":str(imc)})