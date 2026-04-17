from django.shortcuts import render
from .models import Aviso

def lista_avisos(request):
    avisos = Aviso.objects.all().order_by('-data_cracao')
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        avisos = avisos.filter(categoria_id=categoria_id)
    
    return render(request, 'mural/lista_avisos.html', {'avisos': avisos})

def detalhe_aviso(request, id):
    aviso = get_object_ou_404( Aviso, id=id)
    return render(request, 'mural/detalhe_aviso.html', {'aviso': aviso})

def criar_aviso(request):
    if request.method == 'POST':
        form = Avisoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Avisoform()
    return render(request, 'mural/fom_aviso.html', {'form': form})