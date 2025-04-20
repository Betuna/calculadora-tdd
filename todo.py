def raiz_cuadrada(n, precision=1e-10):
    if n < 0:
        raise ValueError("No existe raíz real de números negativos")
    if n == 0:
        return 0
   
    aproximacion = n
    while True:
        nueva_aproximacion = 0.5 * (aproximacion + n / aproximacion)
        if abs(aproximacion - nueva_aproximacion) < precision:
            return nueva_aproximacion
        aproximacion = nueva_aproximacion

def test_exponencial():
    assert exponencial(0) == pytest.approx(1, 0.001)
    assert exponencial(1) == pytest.approx(2.71828, 0.001)
    assert exponencial(2) == pytest.approx(7.389056, 0.001)


def exponencial(x, iteraciones=20):
    resultado = 1.0
    termino = 1.0
    for n in range(1, iteraciones):
        termino *= x / n
        resultado += termino
    return resultado



# Mejorar la precisión en raíz cuadrada
def raiz_cuadrada(n, precision=1e-12, max_iter=100):
    if n < 0:
        raise ValueError("No existe raíz real de números negativos")
    if n == 0:
        return 0
   
    aproximacion = n
    for _ in range(max_iter):
        nueva_aproximacion = 0.5 * (aproximacion + n / aproximacion)
        if abs(aproximacion - nueva_aproximacion) < precision:
            return nueva_aproximacion
        aproximacion = nueva_aproximacion
    return aproximacion



# calculadora/operaciones.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def raiz_cuadrada(n, precision=1e-12, max_iter=100):
    if n < 0:
        raise ValueError("No existe raíz real de números negativos")
    if n == 0:
        return 0
   
    aproximacion = n
    for _ in range(max_iter):
        nueva_aproximacion = 0.5 * (aproximacion + n / aproximacion)
        if abs(aproximacion - nueva_aproximacion) < precision:
            return nueva_aproximacion
        aproximacion = nueva_aproximacion
    return aproximacion

def exponencial(x, iteraciones=30):
    resultado = 1.0
    termino = 1.0
    for n in range(1, iteraciones):
        termino *= x / n
        resultado += termino
    return resultado