from django.urls import path
from . import views

urlpatterns = [  
    path('', views.liste_vente, name='liste_ventes'), 
    path('ajouter_produit/', views.ajouter_produit, name='ajouter_produits'), 
    path('Ajouter/', views.Ajouter_vente, name='Ajouter_vente'),  
    path('dashboard/', views.tableau_de_bord, name='tableau_de_bord'),  
    
]
