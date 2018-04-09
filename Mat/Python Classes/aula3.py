import numpy as np
print("Exercício 1")
x = np.array ([3,2] )

y = np.array([5 , 1])

z  = x + y
print("Matriz de X" , x)
print("Matriz de Y" , y)
print("Resultado da soma da matriz" , z)

print("\nExercício2")
x = np.array ([3,2] )

y = np.array([5 , 1])

z  = x - y
print("Matriz de X" , x)
print("Matriz de Y" , y)
print("Resultado da subtração da matriz" , z)

print("\nExercíco3 Produtos Escalar Vertores")

x = np.array([1 , 2 , 3])

y = np.array([-7 , 8 , 9])

z = np.dot ( x , y)

print(z)
print()

dot = np.dot ( x , y)

x_modulus = np.sqrt((x * x) .sum())
y_modulus = np.sqrt((y * y) .sum())

cos_angle = dot / x_modulus / y_modulus

angle = np.arccos(cos_angle)

print(angle)  # unidade de radiandos

graus = angle * 360 / 2 / np.pi

print(graus)  # Resultado em graus

print("\nutilizando outra formula")
z2 = x_modulus * y_modulus * cos_angle # Outra formula
print(z2)


print("Exerccoi 4 Calcule o produto vetorial A x B ")
print(" A = 0 , 0 , 1 \n B =  0 , 1 , 0" )

a = np.array([ 0 , 0 , 1])
b = np.array([0 , 1 , 0])

c = np.cross( a , b) # Cross = Produto Ortogonal
d = np.cross( b , a)

print("Valor de C" ,c ,"\nValor de D", d)

print("\nExercico 5")

A = np.array([1 , 2 , 1])
B = np.array([4 , 1 , 2])

C = np.cross(A , B)
D = np.cross(B , A)

print("Resultado de A" , C, "\nResultado de B" , D)

print("\nExercício 6")




