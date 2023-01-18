
rows_num = int(input("Ingrese el numero de filas: "))
colum_num = int(input("Ingrese el numero de columnas: "))

matrix = []
count_rows = 0
count_colum = 0

for rows in range(1,rows_num + 1):
    list_matrix= []
    if rows % 2 != 0 :
        for column in range(1,colum_num + 1):
            list_1 = count_rows + column
            list_matrix.append(list_1)
        matrix.append(list_matrix)
        count_colum = list_matrix[-1]

    if rows % 2 == 0:
        for column in range(1,colum_num + 1):
            list_1.append(count_colum + column)
        list_1= list_1[ : :-1]
        matrix.append(list_1)
        count_rows = list_1[0]
        
print(matrix)