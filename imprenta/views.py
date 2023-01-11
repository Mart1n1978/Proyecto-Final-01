from django.shortcuts import render
from django.views.generic import ListView, CreateView
from imprenta.models import Post
from django.urls import reverse_lazy


def index(request):
        return render(request, "imprenta/index.html", {})


class PostList(ListView):
        model = Post

class PostCrear(CreateView):
        model = Post
        success_url = reverse_lazy("imprenta-listar")
        fields =  '__all__'

