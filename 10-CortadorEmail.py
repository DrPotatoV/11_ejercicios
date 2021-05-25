print("Separador de email (SLICER EMAIL) \n")
correo = input("Introduce tu correo electronico: ").strip("")

separador = correo.index('@')
usuario = correo[:separador]
dominio = correo[separador+1:]

print("Correo: " + correo)
print("Usuario: " + usuario)
print("Dominio: " + dominio)