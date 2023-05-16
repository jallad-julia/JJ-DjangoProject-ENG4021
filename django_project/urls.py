"""
  A lista de 'urlpatterns' conecta URLs (arquivos html na pasta templates) com as views. 
  Para importar uma views: from nomedoapp import views. 
  Para adicionar uma URL à lista: path('', views.nomedafunção, name='exemplo'). Obs: Só um path pode ter '' vazio. A string colocada nesse espaço indicará  a extensão a ser adicionada ao link da página para acessar esse URL.
"""

from django.contrib import admin
from django.urls import path
from appAtiv2JJ import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= 'home'),
    path('listas/',views.list_tecnicos_ranking,name='list_tec_rank'),
    path('ranking/create/',views.create_ranking),
    path('listas/create/', views.create_listas),
    path('tecnicos/edit/<tecnico_id>',views.update_tecnicos),
    path('tecnicos/delete/<tecnico_id>', views.delete_tecnicos),
    path('atletas/edit/<atleta_id>',views.update_atletas),
    path('atletas/delete/<atleta_id>', views.delete_atletas)

]
