def devolver_distintos(*args):
    # Verificar que se pasen exactamente tres números
    if len(args) != 3:
        return "Debes pasar exactamente tres números."

    valor = sum(args)  # Sumar los tres números

    # Si la suma es mayor a 15, devolver el número mayor
    if valor > 15:
        return max(args)
    # Si la suma es menor a 10, devolver el número menor
    elif valor < 10:
        return min(args)
    # Si la suma está entre 10 y 15, devolver el número intermedio
    else:
        return sorted(args)[1]  # El número intermedio es el segundo en una lista ordenada

# Pruebas
print(devolver_distintos(1, 2, 3))  # La suma es 6, menor que 10, devuelve 1
print(devolver_distintos(4, 6, 9))  # La suma es 19, mayor que 15, devuelve 9
print(devolver_distintos(4, 5, 6))  # La suma es 15, devuelve 5
print(devolver_distintos(2, 2, 2))  # La suma es 6, menor que 10, devuelve 2
print(devolver_distintos(3, 3, 3))  # La suma es 9, menor que 10, devuelve 3

