from django.urls import path
from imovel import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('perfil-imoveis/', views.perfil_imoveis, name='perfil_imoveis'),
    path('item-imovel/<int:id_imovel>', views.item_imovel, name='item_imovel'),
    path('Adicionar-imovel/', views.AdicionarImovelView.as_view(), name='adicionar_imovel'),
]