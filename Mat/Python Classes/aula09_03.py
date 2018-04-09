import numpy as np



a = np.array  ([[2,1,1],[1,3,2],[1,0,0]])

b = np.array ([4 , 5 , 6])


print("Solutions: \n" , np.linalg.solve(a,b)) # Para Calcular a expressão linear

print("Exercicio2")

c = np.array ([[3,2,1], [1,3,2] ,[1,2,3]])
d= np.array ([7,8,9])

print("Resultado:\n" , np.linalg.solve(c,d))

print()
print()
print()

z = np.zeros( (8,8) , dtype= int) # Resolução Exercicio2
z[1::2,::2] = 1
z[::2,1::2] = 1
print(z)
# Explicar o código

print()
print()
print()

print(np.unravel_index(10 ,(6,7,8))) # Resolução do exercício 3
# Explicar o código