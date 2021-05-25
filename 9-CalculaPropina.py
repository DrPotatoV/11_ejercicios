subtotal = float (input("¿Introduzca el total de la cuenta: "))
pers = int (input("¿Cuantas personas hay en la mesa?"))
#Calcular el 18% 20% y 25%

subtotal18= subtotal*0.18
subtotal20= subtotal*0.20
subtotal25= subtotal*0.25
total18= subtotal*1.18
total20= subtotal*1.20
total25= subtotal*1.25

print("El total de la factura es: " + str(subtotal))
print("El total de la factura aplicando propinas es de: "
+"\n" + str(total18) + " Aplicando " + str(subtotal18) + " con 18% de propinas"
+"\n" + str(total20) + " Aplicando " + str(subtotal20) + " con 20% de propinas"
+"\n" + str(total25) + " Aplicando " + str(subtotal25) + " con 25% de propinas")

print("A cada comenzal le tocará pagar: "
+"\n" + str(subtotal18/pers) + " con 18% de propinas"
+"\n" + str(subtotal20/pers) + " con 20% de propinas"
+"\n" + str(subtotal25/pers) + " con 25% de propinas")
