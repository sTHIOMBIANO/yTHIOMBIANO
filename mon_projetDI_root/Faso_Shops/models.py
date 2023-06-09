from django.db import models

# Create your models here.

class Categorie(models.Model):
    name=models.CharField(max_length=500)
    date_ajout=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-date_ajout']

    def __str__(self):
        return f"{self.name}"

class Produit(models.Model):
    titre=models.CharField(max_length=500)
    prix=models.FloatField()
    description=models.TextField()
    categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="static/album",blank=True)
    date_ajout=models.DateTimeField(auto_now=True)


    class Meta:
        ordering=['-date_ajout']

    def __str__(self):
        return f"{self.titre}"


class Commande(models.Model):
    items=models.CharField(max_length=500)
    total=models.CharField(max_length=300)
    nom = models.CharField(max_length=500)
    prenom = models.CharField(max_length=500)
    email = models.EmailField()
    ville = models.CharField(max_length=300) 
    pays = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    produit=models.ForeignKey(Produit,on_delete=models.CASCADE,null=True)
    date_commande=models.DateTimeField(auto_now=True)


    class Meta:
        ordering=['-date_commande']


    def __str__(self):
        return f"{self.nom}"


class Pretporter(models.Model):
    title=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='static/album')
    date_pret=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-date_pret']


    def __str__(self):
        return f"{self.title}"


class Pagne(models.Model):
    libelle=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='static/album')
    date_pagne=models.DateTimeField(auto_now=True)


    class Meta:
        ordering=['-date_pagne']


    def __str__(self):
        return f"{self.libelle}"

