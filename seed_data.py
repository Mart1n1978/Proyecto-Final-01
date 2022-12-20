from ejemplo.models import Automovil, Familiar, Mascota
Familiar(nombre="Silvina", direccion="Carlos Pellegrini 30", numero_pasaporte=31300269).save()
Familiar(nombre="Fatiga", direccion="Santiago del estero 1676", numero_pasaporte=20211211).save()
Familiar(nombre="Rosa", direccion="General Paz 709", numero_pasaporte=10991019).save()
Familiar(nombre="Edgar", direccion="2da casa despues de la tranquera", numero_pasaporte=10551541).save()
Mascota(nombre="Fatiga", raza="gato", edad=2).save()
Automovil(marca="Toyota", modelo="Corolla", anio=2006).save()

print("Se cargo con éxito los usuarios de pruebas")

