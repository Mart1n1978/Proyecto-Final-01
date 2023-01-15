from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from imprenta.models import Post
from imprenta.forms import UsuarioForm
from imprenta.models import Avatar, Post, Mensaje
from django.contrib.auth.admin import User

@login_required#si se pone @login_required en cualquier funcion entonces se debera loguear para poder entrar
def index(request):
    posts = Post.objects.order_by('-publicado_el').all()
    return render(request, "imprenta/index.html", {"posts": posts})

class PostListar(ListView): #esto lo tiene distinto denise
    model = Post  

class PostDetalle(LoginRequiredMixin, DetailView):
    model = Post

class PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("imprenta-listar")
    fields =  '__all__'

class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("imprenta-listar")

class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("imprenta-listar")
    fields = "__all__"

class PostDetalle(DetailView):
    model = Post

class UserSignUp(CreateView): #con esto hacemos la creacion de usuario
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy("imprenta-listar")

class UserLogin(LoginView):
    next_page = reverse_lazy('imprenta-listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('imprenta-listar')

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy('imprenta-listar')

class UserActualizar(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy("imprenta-listar")

class MensajeDetalle(LoginRequiredMixin, DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje  

class MensajeCrear(CreateView):
    model = Mensaje
    success_url = reverse_lazy("imprenta-mensajes-crear")
    fields = ['nombre', 'email', 'texto']

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("imprenta-mensajes-listar")

def about(request):
    return render(request, "imprenta/about.html")