import random

elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lenght = int(input("Introduzca la longitud de la contraseña: "))

password = ""

for i in range(lenght):
    password += random.choice(elements)

print("La contraseña generada es: ", password)
