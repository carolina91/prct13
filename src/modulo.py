#!enconding: UTF-8
import sys
import math


PI35DT= 3.1415926535897931159979634685441852

#utilizacion de una funcion calcular_xi para obtener los xi
def calcular_xi (n, i):
 xi = (i - 1.0/2.0) / n
 return xi
 
 #utilizacion de una funcion calcular_pi
def calcular_pi(n):
   PI35 = 3.1415926535897931159979634685441852
   sumatorio = 0.0
   ini = 0
   intervalos = 1.0 / float (n)
   for i in range(n):
     x_i = ((i+1) - 1.0/2.0) / n
     fx_i = 4.0 / (1.0 + x_i * x_i)
     ini += intervalos
     sumatorio += fx_i
   valor_pi = sumatorio / n
   return (valor_pi)
   
def error (n, aproximaciones, umbral):
   intervalo = n
   
   lista = []
   for i in range (aproximaciones):
     valor = calcular_pi (intervalo)
     intervalo += n
     lista.append (valor)
     
   PI35 = []
   for i in range (aproximaciones):
     PI35.append(PI35DT)
     
   diferencia = []
   for i in range (aproximaciones):
     dif = abs (PI35DT - lista[i])
     diferencia.append (dif)
     
   correcto = 0
   for i in range (aproximaciones):
    if (diferencia[i] <= umbral):
       correcto = correcto + 1
   porcentaje = 100.0 *(1.0-(float(correcto) / float(aproximaciones)))
   return (porcentaje)
 
if(__name__=="__main__"):
#programa principal
 argumentos = sys.argv[1:] #desde la posicion uno hasta el final
 print argumentos
 if (len(argumentos) == 3):
    n = int (argumentos[0])
    aproximaciones = int (argumentos[1])
    umbral = float (argumentos[2])
 else:
    print "introduzca el numero de intervalos (n > 0):"
    n = int (raw_input())
    print "introduzca el numero de aproximaciones:"
    aproximaciones = int (raw_input())
    print "Introduzca el umbral de error"
    umbral = float (raw_input())
 if (n>0):
   porcentaje = error (n, aproximaciones, umbral)
   print " el porcentaje de fallos es del ",porcentaje
 else:
   print "el valor de los intervalos debe ser mayor que cero"