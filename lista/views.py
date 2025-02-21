from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm

# 📌 Lista todas as tarefas
def lista_tarefas(request):
    tarefas = Tarefa.objects.all().order_by('-criada_em')
    return render(request, 'lista/lista_tarefas.html', {'tarefas': tarefas})

# 📌 Adiciona uma nova tarefa
def adicionar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'lista/form_tarefa.html', {'form': form})

# 📌 Edita uma tarefa
def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'lista/form_tarefa.html', {'form': form})

# 📌 Exclui uma tarefa
def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('lista_tarefas')
    return render(request, 'lista/confirmar_exclusao.html', {'tarefa': tarefa})
