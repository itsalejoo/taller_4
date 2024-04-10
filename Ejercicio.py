import numpy as np  #se importa la biblioteca de numpy y se le asigna un alias "np"
import matplotlib.pyplot as plt #se importa la biblioteca de matplotlib y se le asigna un alias "plt"
def mandelbrot(h, w, maxit=20, r=2):       #se definen 4 valores para definir un "parametro" para Maxit y "r" devuelve una imagen en el tamaño (h,w)
 
    x = np.linspace(-2.5, 1.5, 4*h+1)  #desde la biblioteca numpy se llamo a la funcion linspace para generar numeros especificos en el "x" multiplicando 4*h y suamdole 1
    y = np.linspace(-1.5, 1.5, 3*w+1)  #desde la biblioteca numpy se llamo a la funcion linspace para generar numeros especificos en el "y" multiplicando 3*w y suamdole 1
    A, B = np.meshgrid(x, y)   #se llamo la funcion meshgrid para crear una  lista de matrices de coordenadas a partir de vectores de coordenadas asignandi el valor de x en A , y en B
    C = A + B*1j #se creo "c" para solicitar el valor en la operacion A+B*1J
    z = np.zeros_like(C)
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**2 + C
        diverge = abs(z) > r                    # who is diverging
        div_now = diverge & (divtime == maxit)  # who is diverging now
        divtime[div_now] = i                    # note when
        z[diverge] = r                          # avoid diverging too much

    return divtime
plt.clf()
plt.imshow(mandelbrot(400, 400))