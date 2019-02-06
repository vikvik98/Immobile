from django.urls import path
from imovel import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('Adicionar-imovel/', views.AdicionarImovelView.as_view(), name='adicionar_imovel'),
]