import math

# Conversión de temperatura de Celsius a Kelvin
def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

# Cálculo de la media de los datos de estatura
def calcular_media(datos):
    total = sum(datos)
    media = total / len(datos)
    return media

# Cálculo de la desviación estándar de los datos de estatura
def calcular_desviacion_estandar(datos, media):
    suma_cuadrados = sum((x - media) ** 2 for x in datos)
    desviacion_estandar = math.sqrt(suma_cuadrados / len(datos))
    return desviacion_estandar

# Cálculo de la suma de los valores menos la media al cuadrado
def calcular_suma_cuadrados(datos, media):
    suma_cuadrados = sum((x - media) ** 2 for x in datos)
    return suma_cuadrados

# Ejemplo de uso

# Conversión de temperatura
temperatura_celsius = 25
temperatura_kelvin = celsius_to_kelvin(temperatura_celsius)
print(f"{temperatura_celsius}°C = {temperatura_kelvin}K")

# Cálculo de la media de estaturas
estaturas = [1.5, 2.2, 1.56, 1.78, 1.82, 1.90, 1.66, 1.91, 1.76, 1.88]
media_estaturas = calcular_media(estaturas)
print(f"La media es: {media_estaturas}m")

# Cálculo de la desviación estándar de estaturas
desviacion_estandar = calcular_desviacion_estandar(estaturas, media_estaturas)
print(f"La desviación estándar es: {desviacion_estandar}")

# Cálculo de la suma de los valores menos la media al cuadrado
suma_cuadrados = calcular_suma_cuadrados(estaturas, media_estaturas)
print(f"La suma de los valores menos la media al cuadrado es: {suma_cuadrados}")
