from django.urls import path
from .views import lista_voo, detalhes_voo, novo_voo, editar_voo, excluir_voo

urlpatterns = [
    path('', lista_voo, name='lista_voos'),
    path('voo/<int:pk>/', detalhes_voo, name='detalhes_voo'),
    path('voo/novo/', novo_voo, name='novo_voo'),
    path('voo/<int:pk>/editar/', editar_voo, name='editar_voo'),
    path('voo/<int:pk>/excluir/', excluir_voo, name='excluir_voo'),
]
