from django.urls import path

from imovel import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('perfil-imoveis/', views.perfil_imoveis, name='perfil_imoveis'),
    path('item-imovel/<int:id_imovel>', views.item_imovel, name='item_imovel'),
    path('adicionar-imovel/', views.AdicionarImovelView.as_view(), name='adicionar_imovel'),
    path('remover-imovel/<int:imovel_id>', views.remover_imovel, name='remover_imovel'),
    path('item-imovel/<int:id>/editar', views.editar_imovel, name='editar_imovel'),
    path('add-proprietario/<int:id>', views.add_proprietario, name='add_proprietario'),
]
