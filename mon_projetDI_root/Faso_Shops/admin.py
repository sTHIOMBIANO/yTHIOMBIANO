from django.contrib import admin
from .models import Categorie,Produit,Commande,Pretporter,Pagne
# Register your models here.
admin.site.site_header="THIOMBIANO"
admin.site.site_title="Dgango"
admin.site.index_title="THIOMBIANO-Developpeur Web"

class AdminCategorie(admin.ModelAdmin):
    list_display=('name','date_ajout')

class AdminProduit(admin.ModelAdmin):
    list_display=('titre','prix','categorie','date_ajout')
    search_fields=('titre',)
    list_editable=('prix','categorie',)


class AdminCommande(admin.ModelAdmin):
    list_display=('items','nom','prenom','email','telephone','total','date_commande')
    search_fields=('nom','prenom',)

class AdminPretporter(admin.ModelAdmin):
    list_display=('title','price','date_pret')

class AdminPagne(admin.ModelAdmin):
    list_display=('libelle','price','date_pagne')


admin.site.register(Categorie,AdminCategorie)
admin.site.register(Produit,AdminProduit)
admin.site.register(Commande,AdminCommande)
admin.site.register(Pretporter,AdminPretporter)
admin.site.register(Pagne,AdminPagne)