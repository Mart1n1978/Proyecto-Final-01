from django.shortcuts import render

def index(request):
        return render(request, "imprenta/index.html", {})
# Create your views here.
