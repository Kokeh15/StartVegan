from django.urls import path
from .views import home, Desayuno, almuerzo , cena, listadesayuno, listacena, listproductos, agregarcena, contacto ,registrarse, eliminarcena, modificarprod, login

urlpatterns = [
    path('', home, name="home"),
    path('desayuno/', Desayuno, name="desayuno"),
    path('almuerzo/', almuerzo, name="almuerzo"),
    path('cena/', cena, name="cena"),
    path('lista-desayuno/', listadesayuno, name= "lista_desayuno"),
    path('lista-cena/', listacena, name= "lista_cena"),
    path('lista-productos/', listproductos, name= "lista_productos"),
    path('agregar-cena/', agregarcena, name= "agregar_cena"),
    path('contacto/',contacto, name="contacto"),
    path('registrarse/',registrarse, name="registrarse"),
    path('eliminar-cena/<id>/', eliminarcena , name="eliminar_cena"),
    path('modificar-pro/<id>/', modificarprod , name="modificar_pro"),
    path('login/', login, name='login'),
]
