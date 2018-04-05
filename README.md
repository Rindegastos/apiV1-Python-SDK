# PYTHON SDK apiV1
Rindegastos PYTHON SDK API documentation

# SDK PYTHON

El SDK PYTHON de Rindegastos te permite rápidamente integrar tus servicios con Rindegastos. Con el SDK podrás autenticarte y consumir los métodos de la API segun tus necesidades sin tener que desarrollar desde cero todo.

#Instrucciones

Lo primero que debes hacer para usar el SDK es descargarlo aquí. Una vez descargado lo único que tienes que hacer es incluir la clase RindeGastos.PYTHON en tu proyecto y hacer uso de sus funciones.

Importante: recuerda que lo primero que debes hacer es tener to Token de Acceso a la API asignado como se indica aquí.

# Ejemplo de uso
Consumir los métodos de la API con el SDK es muy simple. A continuación te explicamos cómo hacerlo para usar el método getExpenses de la API.s

``` PYTHON
import Sdkrindegastos
import json

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNjEiLCJjb21wYW55X2lkIjoiMTA5IiwicmFuZG9tIjoicmFuZEFQSTVhYTgzZTI4OWY0NWQzLjUwNDczNzY4In0.arDxsQlJlssjrUoh2Dx_72-wDm_RSYXDSO7s0pkFtIc"
r = Sdkrindegastos.Rindegastos(token)
params = {}
try:
    policiesResult = r.getUsers(params)
    print(policiesResult.status)
    print(policiesResult.reason)
    print(policiesResult.read())
except ValueError:
    print(ValueError)

```