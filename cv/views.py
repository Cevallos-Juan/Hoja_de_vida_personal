from django.shortcuts import render
from .models import Perfil, Educacion, Experiencia, Habilidad, Referencia, Certificado, Proyecto

def cv_view(request):
    perfil = Perfil.objects.first()

    educaciones = Educacion.objects.all()
    experiencias = Experiencia.objects.all()
    habilidades = Habilidad.objects.all()
    referencias = Referencia.objects.all()

    certificados = []
    proyectos = []

    if perfil:
        certificados = perfil.certificados.all()
        proyectos = perfil.proyectos.all()

    context = {
        'perfil': perfil,
        'educaciones': educaciones,
        'experiencias': experiencias,
        'habilidades': habilidades,
        'certificados': certificados,
        'proyectos': proyectos,
        'referencias': referencias,
    }

    return render(request, 'cv/cv.html', context)


def home(request):
    perfil = Perfil.objects.first()
    return render(request, 'cv/home.html', {'perfil': perfil})
