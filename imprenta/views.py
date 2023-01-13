from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from imprenta.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from imprenta.forms import UsuarioForm

#si se pone @login_required en cualquier funcion entonces se debera loguear para poder entrar
def index(request):
    return render(request, "imprenta/index.html", {})

class PostListar(ListView):
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

class UserSignUp(CreateView): #con esto hacemos la creacion de usuario
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy("imprenta-listar")

class UserLogin(LoginView):
    next_page = reverse_lazy('imprenta-listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('imprenta-listar')
