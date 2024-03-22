#Problema 1  / 8 ptos x4 pruebas / 32 puntos
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
#La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)
t1 = tuple(input().split())
t2 = tuple(input().split())

t1_casted = []
t2_casted = []

for i in t1:
    try:
        t1_casted.append(eval(i))
    except:
        t1_casted.append(i)

for i in t2:
    try:
        t2_casted.append(eval(i))
    except:
        t2_casted.append(i)

print(tuple(t2_casted + t1_casted + t2_casted))
