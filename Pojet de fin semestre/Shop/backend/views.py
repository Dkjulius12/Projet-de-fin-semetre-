from django.shortcuts import render, redirect
from .models import Produit, Vente
from .form import VenteForm
from django.db.models import Sum
from django.views.generic import ListView


class Affichage(ListView):
    template_name = 'home.html'
    queryset= Produit.objects.all()

def ajouter_produit(request):
    return render(request, 'backend/ajouter_produit.html') 

def Ajouter_vente(request):
    if request.method == 'POST':
        form = VenteForm(request.POST)
        if form.is_valid():
            vente = form.save(commit=False)
            vente.produit.quantite -= vente.quantite
            vente.produit.save()
            vente.save()
            return redirect('liste_vente')
    else:
        form = VenteForm()

    return render(request, 'backend/Ajouter_vente.html', {'form': form})

def liste_vente(request):
    ventes = Vente.objects.all().order_by('-date_vente')
    return render(request, 'backend/liste_ventes.html', {'ventes': ventes})

def tableau_de_bord(request):
    total_produits = Produit.objects.aggregate(total=Sum('quantite'))['total'] or 0
    total_ventes = Vente.objects.aggregate(total=Sum('quantite'))['total'] or 0
    produit_top = Vente.objects.values('produit__nom').annotate(total=Sum('quantite')).order_by('-total').first()

    return render(request, 'backend/tableau_de_bord.html', {
        'total_produits': total_produits,
        'total_ventes': total_ventes,
        'produit_top': produit_top
    })

