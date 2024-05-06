import fibo # importa el modulo fibo.py
from modulos_dos import suma, multiplicacion
import modulos_tres as tres

fibo.fib(1000) # llama a la funcion fib() del modulo fibo.py

fibo.fib2(100) # llama a la funcion fib2() del modulo fibo.py
print(fibo.fib2(100))

print(fibo.__name__)

fib = fibo.fib
fib(500)

# Suma
suma(10, 5)

# Multiplicacion
print(multiplicacion(10, 5))

# Resta
tres.resta(10, 5)

# Division
print(tres.division(10, 5))

