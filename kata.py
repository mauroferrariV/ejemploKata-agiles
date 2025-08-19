#Suma los números en una string separados por comas.
#Una string vacía devuelve 0.
#
def suma(cadena):
  if cadena == "":
        return 0
  caracteres = cadena.split(",")
  for c in caracteres :
    if not c.lstrip("-").isdigit():  # validación de cada número
      raise ValueError(f"Valor inválido: '{c}' (solo números permitidos)")
  return sum(int(c) for c in caracteres)

