number_of_rows_and_columns = int(input("Introduzca un numero de filas y columnas par:\n"))

value_numbers  = 0

matrix = []

list = []

counter_one = 0

counter_two= 0

for r in range(1,number_of_rows_and_columns+1):
    list = []
    for c in range(1,number_of_rows_and_columns+1):
        value_numbers  += 1
        list.append(value_numbers )
    matrix.append(list) 

value_numbers  = 0
for r in range(1,number_of_rows_and_columns+1):
    list = []
    for c in range(1,number_of_rows_and_columns+1):
        value_numbers += 1
        list.append(value_numbers )

    if r % 2 != 0:
        matrix [counter_one] = list 
        counter_one += 1

    elif r % 2 == 0: 
        counter_two -= 1
        matrix[counter_two] = list 

print (matrix)