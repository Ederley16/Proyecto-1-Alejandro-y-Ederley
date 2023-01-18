num_row_and_colum = int(input("Ingrese el numero de columnas y filas: ")) 

matrix = []
#list = []
count_one = 0
count_two = 0

for i in range(1,num_row_and_colum + 1):
    value_num = 0
    for j in range(1, num_row_and_colum + 1):
        value_num += 1
        list.append(value_num)
    matrix.append(list)

if i%2 != 0:
    matrix[count_one] = list
    count_one += 1

elif i%2 == 0:
    count_two -= 1
    matrix[count_two] = list

print(matrix)
