import numpy as np
import matplotlib.pyplot as plt


data1 = [1,1,5,2]
data2 = [ 3,4,4,0]
x = 10*np.array(range(len(data1)))

plt.plot( x, data1, 'go') # green bolinha
plt.plot( x, data1, 'k-', color='orange') # linha pontilha orange

plt.plot( x, data2, 'r^') # red triangulo
plt.plot( x, data2, 'k--', color='blue')  # linha tracejada azul

plt.title("Mais incrementado")

plt.grid(True)
plt.xlabel("eixo horizontal")
plt.ylabel("que legal")
plt.show()
