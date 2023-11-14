from django.shortcuts import render, get_object_or_404, redirect
from .models import Voo
from .forms import VooForm


def lista_voo(request):
    voos = Voo.objects.all()
    return render(request, 'lista_voos.html', {'voos': voos})


def detalhes_voo(request, pk):
    voo = get_object_or_404(Voo, pk=pk)
    return render(request, 'detalhes_voo.html', {'voo': voo})


def novo_voo(request):
    if request.method == "POST":
        form = VooForm(request.POST)
        if form.is_valid():
            voo = form.save(commit=False)
            voo.save()
            return redirect('detalhes_voo', pk=voo.pk)
    else:
        form = VooForm()
    return render(request, 'editar_voo.html', {'form': form})


def editar_voo(request, pk):
    voo = get_object_or_404(Voo, pk=pk)
    if request.method == "POST":
        form = VooForm(request.POST, instance=voo)
        if form.is_valid():
            voo = form.save(commit=False)
            voo.save()
            return redirect('detalhes_voo', pk=voo.pk)
    else:
        form = VooForm(instance=voo)
    return render(request, 'editar_voo.html', {'form': form})


def excluir_voo(request, pk):
    voo = get_object_or_404(Voo, pk=pk)
    voo.delete()
    return redirect('lista_voos')
