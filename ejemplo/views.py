from django.shortcuts import render, get_object_or_404
from ejemplo.models import Familiar, Automovil, Mascota
from ejemplo.forms import Buscar, BuscarAutomoviles, BuscarMascotas, FamiliarForm, AutomovilForm, MascotaForm # <--- NUEVO IMPORT
from django.views import View # <-- NUEVO IMPORT 

def index(request):
    return render(request, "ejemplo/saludar.html") 

def saludar_a(request, nombre):
    return render (request,
    'ejemplo/saludar_a.html',
    {'nombre': nombre}
    )

def sumar(request, a, b):
    return render (request,
    'ejemplo/sumar.html',
    {'a':a,
    'b': b,
    'resultado':a+b
    }
    )

def buscar(request):
    lista_de_nombre = ['German', 'Daniel', 'Martin']
    query = request.GET['q']
    if query in lista_de_nombre:
        indice_de_resultado = lista_de_nombre.index(query)
        resultado = lista_de_nombre[indice_de_resultado]
    else:
        resultado = 'no hay match'
    return render(request, 'ejemplo/buscar.html', {'resultado': resultado})

def mostrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

def mostrar_automoviles(request):
    lista_automoviles = Automovil.objects.all()
    return render(request, "ejemplo/automoviles.html", {"lista_automoviles": lista_automoviles})

def mostrar_mascotas(request):
    lista_mascotas = Mascota.objects.all()
    return render(request, "ejemplo/mascotas.html", {"lista_mascotas": lista_mascotas})


class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarFamiliar(View):
    form_class = FamiliarForm
    template_name = 'ejemplo/actualizar_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
    def get(self, request, pk): 
        familiar = get_object_or_404(Familiar, pk=pk)
        form = self.form_class(instance=familiar)
        return render(request, self.template_name, {'form':form,'familiar': familiar})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
    def post(self, request, pk): 
        familiar = get_object_or_404(Familiar, pk=pk)
        form = self.form_class(request.POST ,instance=familiar)
        if form.is_valid():
            form.save()
            msg_exito = f"se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial) # borra formulario
            return render(request, self.template_name, {'form':form, 
                                                      'familiar': familiar,
                                                      'msg_exito': msg_exito})
      
        return render(request, self.template_name, {"form": form})

class BorrarFamiliar(View):
    template_name = 'ejemplo/familiares.html'
      
    def get(self, request, pk): 
        familiar = get_object_or_404(Familiar, pk=pk)
        familiar.delete()
        familiares = Familiar.objects.all()
        return render(request, self.template_name, {'lista_familiares': familiares})

class BuscarMascota(View):
    form_class = BuscarMascotas
    template_name = 'ejemplo/buscar_mascota.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_mascotas = Mascota.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_mascotas':lista_mascotas})
        return render(request, self.template_name, {"form": form})

class AltaMascotas(View):

    form_class = MascotaForm
    template_name = 'ejemplo/alta_mascotas.html'
    initial = {"nombre":"", "raza":"", "edad":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito la mascota {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarMascota(View):
  form_class = MascotaForm
  template_name = 'ejemplo/actualizar_mascota.html'
  initial = {"nombre":"", "raza":"", "edad":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      mascota = get_object_or_404(Mascota, pk=pk)
      form = self.form_class(instance=mascota)
      return render(request, self.template_name, {'form':form,'mascota': mascota})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      mascota = get_object_or_404(Mascota, pk=pk)
      form = self.form_class(request.POST ,instance=mascota)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito la mascota {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'mascota': mascota,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class BuscarAutomovil(View):
    form_class = BuscarAutomoviles
    template_name = 'ejemplo/buscar_automoviles.html'
    initial = {"marca":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            marca = form.cleaned_data.get("marca")
            lista_automoviles = Automovil.objects.filter(marca__icontains=marca).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_automoviles':lista_automoviles})
        return render(request, self.template_name, {"form": form})

class AltaAutomoviles(View):

    form_class = AutomovilForm
    template_name = 'ejemplo/alta_automoviles.html'
    initial = {"marca":"", "modelo":"", "año":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el automovil de {form.cleaned_data.get('marca')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarAutomovil(View):
  form_class = AutomovilForm
  template_name = 'ejemplo/actualizar_automovil.html'
  initial = {"marca":"", "modelo":"", "año":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      automovil = get_object_or_404(Mascota, pk=pk)
      form = self.form_class(instance=automovil)
      return render(request, self.template_name, {'form':form,'automovil': automovil})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      automovil = get_object_or_404(Automovil, pk=pk)
      form = self.form_class(request.POST ,instance=automovil)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el automovil {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'automovil': automovil,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})