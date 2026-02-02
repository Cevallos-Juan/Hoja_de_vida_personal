from django.shortcuts import render
from .models import Perfil, Educacion, Experiencia, Habilidad, Reconocimiento, Referencia, Certificado, Proyecto, Reconocimiento, Garaje

def cv_view(request):
    perfil = Perfil.objects.first()

    educaciones = Educacion.objects.all()
    experiencias = Experiencia.objects.all()
    habilidades = Habilidad.objects.all()
    referencias = Referencia.objects.all()
    reconocimientos = Reconocimiento.objects.all()
    garajes = Garaje.objects.all()

    certificados = []
    proyectos = []

    if perfil:
        certificados = perfil.certificados.all()
        proyectos = perfil.proyectos.all()

     # 🔥 AQUÍ ESTÁ LA CLAVE
    for r in reconocimientos:
        if r.archivo:
            r.es_pdf = r.archivo.url.lower().endswith('.pdf')
        else:
            r.es_pdf = False

    context = {
        'perfil': perfil,
        'educaciones': educaciones,
        'experiencias': experiencias,
        'habilidades': habilidades,
        'certificados': certificados,
        'proyectos': proyectos,
        'reconocimientos': reconocimientos,
        'garajes': garajes,
        'referencias': referencias,
    }

    return render(request, 'cv/cv.html', context)


def home(request):
    perfil = Perfil.objects.first()
    return render(request, 'cv/home.html', {'perfil': perfil})

