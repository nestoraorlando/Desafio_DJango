from ejemplo.models import Familiar

Familiar(nombre="Néstor", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Alejandro", direccion="Rio Parana 745", numero_pasaporte=456456).save()
Familiar(nombre="José", direccion="Rio Parana 745", numero_pasaporte=789789).save()
Familiar(nombre="Catalina", direccion="Rio Parana 745", numero_pasaporte=147147).save()

print("Se cargo con éxito los usuarios de prueba")