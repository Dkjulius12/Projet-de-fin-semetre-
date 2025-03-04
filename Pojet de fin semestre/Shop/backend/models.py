from django.db import models

from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=200)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.PositiveIntegerField()
    date_ajouts = models.DateTimeField(auto_now_add=True)

    class Meta :
        ordering = ['-date_ajouts']

    def __str__(self):
        return f"{self.nom} - {self.categorie.nom}"

class Vente(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    date_vente = models.DateTimeField(auto_now_add=True)
    prix_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Vente de {self.quantite} {self.produit.nom} le {self.date_vente}"
    
class Client(models.Model):
    nom_client = models.CharField(max_length=255)

class Facture(models.Model):
    nom_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_facture = models.DateTimeField(auto_now_add=True)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantité = models.IntegerField()
    prix_total = models.ForeignKey(Vente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Facture de {self.nom_client} "

