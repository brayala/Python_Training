# 2nd Project / Python training
# 04.19.2022

#Cocohevere cow calculartor

print("Bueno, llegó la hora de la vaca, así que soltando el Tebillegar...")

#Definción del precio de la botella
precio = input("En cuanto sale la jugada? $")
precio_as_float = float(precio)

#Socpe de la pea
Qty = input("Cuantas botellas vamos a samparnos? ")
Qty_as_int = int (Qty)

#Cantidad de coles
Coles = input("Levanten la mano los que van a tomar? ")
Coles_as_int = int (Coles)

Tebille = float (precio_as_float * Qty_as_int / Coles_as_int)
round (Tebille, 2 )

Msj = f"Papi, cayéndose del bus con $ {Tebille} por cabeza..."

print(Msj)