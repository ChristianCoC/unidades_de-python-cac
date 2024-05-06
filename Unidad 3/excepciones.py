"""Excepciones
try: Ejecuta el bloque de instrucciones
except: Ejecuta este código solo si arriba hay una excepción
else: Ejecuta el bloque de instrucciones si no hay excepciones
finally: Ejecuta el bloque de instrucciones siempre"""


def division(dividendo, divisor):
    try:
        return dividendo / divisor
    except ZeroDivisionError:
        return "No se puede dividir entre cero"
    except TypeError:
        return "No se puede realizar la operación"
    except Exception:
        return "Ocurrió un error"
    """else:
        return ("Operación exitosa")"""
    """finally:
        print ('Fin de la operación')"""


print(division(10, 0))
print(division(10, 2))

# Excepciones personalizadas


class DivisorNegativoError(Exception):
    """Error de divisor negativo"""

    pass


def division_numeros_enteros(dividendo, divisor):
    try:
        if divisor < 0:
            raise DivisorNegativoError("No se divide por un numero negativo")
        resultado = dividendo / divisor
        return resultado
    except TypeError:
        return "Datos incorrectos"
    except ZeroDivisionError:
        return "No se puede dividir entre cero"
    except Exception as error:
        return f"Error: {error}"


print(division_numeros_enteros(100, 10))

# Aserciones


def sumar_enteros(a, b):
    try:
        assert isinstance(a, int) and isinstance(
            b, int
        ), "Ambos datos deben ser enteros"
        return a + b
    except AssertionError as error:
        return f"Error: {error}"


print(sumar_enteros(10.5, 20))
