
def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo.

    Parámetros:
        base (int o float): Base del triángulo.
        altura (int o float): Altura del triángulo.

    Retorna:
        int o float: Área calculada del triángulo.

    Excepciones:
        TypeError: Si los valores no son numéricos.
        ValueError: Si la base o altura son menores o iguales a cero.
    """

    if type(base) not in (int, float) or type(altura) not in (int, float):
        raise TypeError("La base y la altura deben ser números")

    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser mayores que cero")

    return (base * altura) / 2
