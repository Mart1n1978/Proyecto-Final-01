"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView 
from ejemplo.views import (
    buscar, index, mostrar_familiares, mostrar_mascotas, mostrar_automoviles,
    saludar_a, sumar, BuscarFamiliar, AltaFamiliar, ActualizarFamiliar, BorrarFamiliar, BuscarMascota,
    AltaMascotas, BuscarAutomovil, AltaAutomoviles, ActualizarAutomovil, ActualizarMascota,
    BorrarMascota, BorrarAutomovil,
)
from imprenta.views import (index, PostDetalle, PostListar,
                            PostCrear, PostBorrar, PostActualizar, 
                            UserSignUp, UserLogin, UserLogout, UserActualizar,
                            AvatarActualizar,
                            MensajeCrear, MensajeBorrar, MensajeListar, MensajeDetalle, about
)
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('saludar-a/<nombre>/', saludar_a),
    path('sumar/<int:a>/<int:b>', sumar),
    path('buscar/', buscar),
    path('mi-familia/', mostrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()), # NUEVA RUTA PARA BUSCAR FAMILIAR
    path('mi-familia/alta', AltaFamiliar.as_view()), # NUEVA RUTA PARA BUSCAR FAMILIAR
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()), # NUEVA RUTA PARA actualizar FAMILIAR
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()), # NUEVA RUTA PARA borrar FAMILIAR
    path('mascotas/', mostrar_mascotas),
    path('automoviles/', mostrar_automoviles),
    path('mascotas/buscar', BuscarMascota.as_view()),
    path('automoviles/buscar', BuscarAutomovil.as_view()),
    path('mascotas/alta', AltaMascotas.as_view()),
    path('automoviles/alta', AltaAutomoviles.as_view()),
    path('mascotas/actualizar/<int:pk>', ActualizarMascota.as_view()),
    path('automoviles/actualizar/<int:pk>', ActualizarAutomovil.as_view()),
    path('mascotas/borrar/<int:pk>', BorrarMascota.as_view()), # NUEVA RUTA PARA borrar FAMILIAR
    path('automoviles/borrar/<int:pk>', BorrarAutomovil.as_view()), # NUEVA RUTA PARA borrar FAMILIAR
    path('imprenta/', index, name="imprenta-index"),
    path('imprenta/about', about, name= 'imprenta-about'),
    path('imprenta/<int:pk>/detalle/', PostDetalle.as_view(), name="imprenta-detalle"),
    path('imprenta/listar/', PostListar.as_view(), name="imprenta-listar"),
    path('imprenta/crear/', staff_member_required(PostCrear.as_view()), name="imprenta-crear"),
    path('imprenta/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="imprenta-borrar"),
    path('imprenta/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="imprenta-actualizar"),
    path('imprenta/signup/', UserSignUp.as_view(), name="imprenta-signup"),
    path('imprenta/login/', UserLogin.as_view(), name="imprenta-login"),
    path('imprenta/logout/', UserLogout.as_view(), name="imprenta-logout"),
    path('imprenta/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="imprenta-avatars-actualizar"),
    path('imprenta/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="imprenta-users-actualizar"),
    path('imprenta/mensajes/crear/', MensajeCrear.as_view(), name="imprenta-mensajes-crear"),
    path('imprenta/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="imprenta-mensajes-detalle"),
    path('imprenta/mensajes/listar/', MensajeListar.as_view(), name="imprenta-mensajes-listar"),
    path('imprenta/mensajes/<int:pk>/borrar/', staff_member_required(MensajeBorrar.as_view()), name = 'imprenta-mensajes-borrar'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)