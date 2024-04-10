#operaciones entre arreglos 

import numpy as np 
a= np.array([-1,10,15,20,25])
print(a)

b=np.array([3,4,7,9,56])
print(b)

c= a+b # se puede sumar +, multiplicar *,restar -, dividir / 
print(c)

d=b**2 #los astericos represtan los exponentes 
print(d)
f=np.sin(b)
print(f)

g=(b<2)
print(g)

h=a@b #@ es para hacer el producto punto 
print(h)

b=b+1 #aqui estamos modificando b
print (b)

#la clase ndarray define:

z=a.sum() # suma todos los elementos del arreglo
print(z)

l= a.min() #saca el numero menor del arreglo 
print(l)

m= a.mean() # saca la media del arreglo.
print(m)

y= np.array([[5,10,-1,20,25], [3,6,4,8,12]])
print(y)
print(y.sum())

print(y.sum(axis=1)) #suma los elementos de la primera fila 
print(y.sum(axis=0)) #se sale de la dimension de los arreglos despues de 2

print(y.min(axis=0)) 

print(y.size) #multipicacion de filas por ejes

print(y.shape) 

print(np.sqrt(y)) #sqrt funcion para sacar la raiz cuadrada de los elementos del arreglo 

print(np.exp(y)) #para sacar el exponencial de los arreglos

y= np.array([[5,10,-1,20,25], [3,6,4,8,12]])
ñ= np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(y)
print(ñ)

#metodos o funciones: 
x= np.add(y,ñ) #sumar + o usar np.add (vamos a tener validacion de la suma o resta)
print(x)

u=np.array([7.8,5.6,3.4]) # a "round" le puede decir cuantos decimales quiero que me redondee (decimals=2)
print(u.round())

print(np.ceil(u)) # es parecido al "round" aproxima al techo 

print(np.gradient(u)) 


