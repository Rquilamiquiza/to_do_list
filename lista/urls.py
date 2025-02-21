from django.urls import path
from .views import lista_tarefas, adicionar_tarefa, editar_tarefa, excluir_tarefa

urlpatterns = [
    path('', lista_tarefas, name='lista_tarefas'),
    path('adicionar/', adicionar_tarefa, name='adicionar_tarefa'),
    path('editar/<int:pk>/', editar_tarefa, name='editar_tarefa'),
    path('excluir/<int:pk>/', excluir_tarefa, name='excluir_tarefa'),
]
