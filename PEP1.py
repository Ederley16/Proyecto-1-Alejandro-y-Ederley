num_ale= int(input("Ingrese la cantidad de número aleatorio que desea generar: ")) 
num_semi= int(input("Ingrese un valor inicial de al menos 4 digitos: "))

def medi(tam,num_semi):    #Funcion para sustraer los 4 digitos centrales.
    lim_s = tam // 2
    lim_i = tam + lim_s
    return str(num_semi)[-lim_i:-lim_s]

def cuadra_medi(num_ale,num_semi):      #Funcion para generar numeros aleatorios
    tam = len(str(num_semi))
    list_alea = []
    for i in range(num_ale): 
        num_semi = num_semi**2
        medi_1 = medi(tam,num_semi)
        list_alea.append(float("0." + medi_1))
    return list_alea

coun = 1
while len(str(num_semi)) < 4 :
    num_semi = input("Vuelva a ingresar un valor:")
    coun += 1
    if coun == 4 :
        print("Ha alcanzado el limite de intentos")
        break

else:
    list = cuadra_medi(num_ale,num_semi)
    print(list)