#importar la biblioteca
import numpy as np

# una forma de crear arreglos ndarray es uasando una lista.
miLista=[3,5,7,9]
miArreglo= np.array(miLista)

#Dimensiones
print(miArreglo.ndim)
print(miArreglo.shape)
print(miArreglo.size)
print(miArreglo.dtype)

miArreglo2= np.array([3,6,7,90])

#crear arreglos de dos dimensiones a partir de listas


miLista3= [(1,3,5,7), (3,8,2,4), (12,78,90,78)]
miArreglo3= np.array(miLista3, dtype= int)
print(miArreglo3.ndim)
print(miArreglo3)






















