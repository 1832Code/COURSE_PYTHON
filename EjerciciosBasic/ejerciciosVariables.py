import math

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    
    Args:
        radio (float): El radio del círculo.
        
    Returns:
        float: El área del círculo.
    """
    area = math.pi * (radio**2)
    return area

# Pedimos al usuario que ingrese el radio del círculo
radio = float(input("Ingresa el radio del círculo: "))

# Llamamos a la función para calcular el área y lo imprimimos
area_circulo = calcular_area_circulo(radio)
print(f"El área del círculo con radio {radio} es: {area_circulo}")

