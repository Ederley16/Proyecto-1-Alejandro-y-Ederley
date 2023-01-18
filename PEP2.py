
H= int(input("Ingrese la profundidad del pozo: "))
Ld = int(input("Ingrese la distancia que asciende el caracol: "))
Ln = int(input("Ingrese la distancia que resbala el caracol: "))

count_day = 1
dis_day = int(Ld - Ln)

while dis_day < H:
    count_day += 1
    dis_day = int(count_day*(Ld - Ln))
print(f"Se tardo {count_day} dias")

if Ld > H:
    print("El caracol ha subido en el primer día")

elif dis_day <= 0 :
    print("El caracol no saldra del pozo")