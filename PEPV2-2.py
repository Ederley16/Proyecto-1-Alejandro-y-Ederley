number_of_terms = int(input("Ingrese la cantidad de terminos a ejecutar:\n"))

result = 0 
if number_of_terms == 1:
    result = (1/(1**6))

elif number_of_terms % 2 == 0 and number_of_terms > 0:
    cicle_number = int(number_of_terms / 2)
    sum_count = -1
    for i in range(1,cicle_number+1):
        sum_count += 1
        result = float(result + (1/((i+sum_count)**6)) - (1/((i+1+sum_count)**6)))

elif not number_of_terms % 2 == 0 and number_of_terms > 0:
    value_even = 0
    cicle_number = int((number_of_terms - 1)/2)
    sum_count =-1
    for i in range(1,cicle_number+1):
        sum_count += 1
        value_even = float(result + (1/((i+sum_count)**6)) - (1/((i+1+sum_count)**6)))
    value_odd = float(1/((number_of_terms)**6))

result = value_even + value_odd
print(f"El resultado de la serie con {number_of_terms} terminos sera")
print(result)
