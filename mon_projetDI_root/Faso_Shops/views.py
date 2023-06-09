from django.shortcuts import render
from django.http import HttpResponse
from .models import Produit,Commande
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ContactForm,UserForm
from django.shortcuts import redirect
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.


#@login_required
def index(request):
	produit_objet=Produit.objects.all()
	#slider=Produit.objects.all()
	item=request.GET.get("items-name")
	if item!= ' ' and item is not None:
		produit_objet=Produit.objects.filter(prix__lte=item)
	paginator=Paginator(produit_objet,6)
	page=request.GET.get('page')
	produit_objet=paginator.get_page(page)
	return render(request,"posts/index.html",{"produit_objet":produit_objet})




def detail(request,id):
	Dproduit=Produit.objects.get(id=id)
	return render(request,"posts/details.html",{"Dproduit":Dproduit})


def affiche(request):
	message=""
	#form=ContactForm()
	if request.method=="POST":
		#form=ContactForm(request.POST)
		item=request.POST.get('item')
		total=request.POST.get('total')
		nom=request.POST.get('nom')
		prenom=request.POST.get('prenom')
		email=request.POST.get('email')
		ville=request.POST.get('ville')
		pays=request.POST.get('pays')
		tel=request.POST.get('tel')
		commande=Commande(items=item,nom=nom,prenom=prenom,email=email,ville=ville,pays=pays,telephone=tel,total=total)
		commande.save()
		
		#if form.is_valid():
		#new=Commande.objects.create(**form.cleaned_data)
		#new.save()
		#form=ContactForm()
		return redirect('verifie')

	return render(request,"posts/afficher.html")

@login_required
def verification(request):
	com=Commande.objects.all()[:1]
	for c in com:
		prenom=c.prenom
	return render(request,"posts/verifivation.html",{"prenom":prenom})

def pagne(request):
	pane=Produit.objects.filter(titre__icontains="Pagnes")
	return render(request,"posts/pagne.html",{"pane":pane})

def porter(request):
	habit=Produit.objects.filter(titre__icontains="Habits")
	return render(request,"posts/pret_a_porter.html",{"habit":habit})



def register(request):
	#form=UserForm()
	if request.method=="POST":
		username=request.POST['username']
		firstname=request.POST['firstname']
		lastname=request.POST['lastname']
		email=request.POST['email']
		password=request.POST['password']
		password1=request.POST['password1']
		if User.objects.filter(username=username):
			messages.error(request,"Ce nom existe déja")
			return redirect('register')
		if User.objects.filter(email=email):
			messages.error(request,request,"Ce email existe déja")
		if not username.isalnum():
			messages.error(request,"le nom d'utilisateur ne doit pas comporter du numerique")
			return redirect('register')
		if password!=password1:
			messages.error(request,"les mots de passe sont differents")
			return redirect('register')

		utilisateur=User.objects.create_user(username,email,password)


		utilisateur.first_name=firstname
		utilisateur.last_name=lastname
		utilisateur.save()
		messages.success(request,"votre compte a été crée avec succés")
		return redirect('create')
		#form=UserForm(data=request.POST)
		#if form.is_valid:
			#form.save()
			#messages.success(request,"Votre compte a bien été crée")
			#form=UserForm()
			#return redirect('create')
		#else:
			#messages.error(request,form.errors)
	return render(request,"posts/register.html")


def connect(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username,password=password)
		if user is not None and user.is_active:
			login(request,user)
			#messages.success(request,"Bienvenu")
			firstname=user.username
			return redirect('index')
		else:
			messages.error(request,"erreur d'autentification")
			return redirect('create')
	return render(request,"posts/login.html")
			

#@login_required
def deconnect(request):
	logout(request)
	messages.success(request,"vous etes deconnecté")
	#return redirect('index')
	return redirect('create')