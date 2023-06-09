from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
	path('',views.index,name='index'),
	#path('',views.carrousel,name='carrousel'),
	path('<int:id>/',views.detail,name='detail'),
	path('pagne/<int:id>/',views.detail,name='detail'),
	path('pret_a_porter/<int:id>/',views.detail,name='detail'),
	path('afficher/',views.affiche,name='affiche'),
	path('verification/',views.verification,name="verifie"),
	path('pagne/',views.pagne,name="pagne"),
	path('pret_a_porter/',views.porter,name="porter"),
	path('register/',views.register,name="register"),
	path("login/",views.connect,name="create"),
	path("deconnect/",views.deconnect,name="deconnect")
	
]



if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)