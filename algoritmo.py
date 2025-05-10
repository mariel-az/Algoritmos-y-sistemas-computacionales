rut = input("Rut?: ")
m = 2
suma = 0
numero = rut[::-1]
for i in numero:
    x = int(i) * m
    suma += x
    m += 1
    if m == 8:
        m = 2

resto = suma % 11
digito = 11 - resto

if digito == 10:
    print("Tu digito verificador es K")
elif digito == 11:
    print("Tu digito verificador es 0")
else:
    print(f"Tu digito verificador es {digito}")