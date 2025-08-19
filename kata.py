#Suma los números en una string separados por comas.
#Una string vacía devuelve 0.
def suma(cadena):
  if cadena == "":
        return 0
  numeros = cadena.split(",")
  numeros = [int(n) for n in numeros]
  return sum(numeros)