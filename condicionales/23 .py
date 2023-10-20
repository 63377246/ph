import os 
os.system("cls")

matematicas = int (input ("Matematicas :"))
fisica = int(input("Fisica : "))

#if matematicas > 17 : propina = 3 * matematicas
#else : propina = matematicas
#if fisica> 16 : propina += 2 * fisica
#else : propina += fisica 

propina = matematicas + fisica / 2
if propina > 17 : propina += 2 * matematicas
if fisica  > 16 : propina +=  fisica * 1.5

promedio = matematicas = ( matematicas + fisica)/ 2
print( f" Propina  = { propina  :.2f}" )
print( f" Promedio = { promedio :.2f}" )
print( f" Reloj    = { 'Si'if promedio >16 else 'No'}" )
