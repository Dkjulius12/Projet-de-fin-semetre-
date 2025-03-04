from django import forms
from .models import Vente, Produit

class VenteForm(forms.ModelForm):
    class Meta:
        model = Vente
        fields = ['produit', 'quantite']

    def clean_quantite(self):
        quantite = self.cleaned_data['quantite']
        produit = self.cleaned_data.get('produit')

        if produit and quantite > produit.quantite:
            raise forms.ValidationError("Stock insuffisant !")
        return quantite
