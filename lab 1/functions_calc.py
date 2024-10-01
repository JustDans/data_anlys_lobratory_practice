def choose_mode():
    while(True):
        print("выберте режим работы:\n1 - Операции над числами\n2 - Операции над над матрицами\n")
        number = input("введите номер режима:")
        match number:
            case '1':
                choose_number_operation()
            case '2':
                choose_matrix_operation()
            case _:
                print ("\nerror некорректный ввод error\n")
                continue
        return
    
def operation(symb):
    while(True):
        num1 = input("Введите первое число:")
        try:
            float(num1)
            break
        except:
            print ("\nerror некорректный ввод error\n")
    while(True):
        num2 = input("Введиет второе число:")
        try:
            float(num2)
            if ((int(num2)==0) and (symb=='/') ):
                print("знаминатель не может быть равен нулю")
                continue
            break
        except:
            print ("\nerror некорректный ввод error\n")
    expres = eval(num1+symb+num2)
    print(f"результат{expres}")

def choose_number_operation():
    while(True):
        print("\nвыберите операцию с числами:\n1 - Сложение\n2 - Вычитание\n3 - Умножение \n4 - Деление\n")
        inp = input ("введите номер операции:")
        if ((len(inp)==1) and (ord(inp)>=ord('1')) and (ord(inp)<=ord('4'))):
            operations = ['+','-','*','/']
            operation(operations[int(inp)-1])
            return 
        else:
            print ("\nerror некорректный ввод error\n")

def choose_matrix_operation():
    while(True):
        print("\nвыберите операцию с числами:\n1 - Сложение\n2 - Вычитание\n3 - Умножение")
        inp = input("введите номер операции")
        try:
            float(inp)
        except:
            print ("\nerror некорректный ввод error\n")
            continue
        match inp:
            case 1.:
                M1 = get_matrix()
                M2 = get_matrix()
                result = matrix_addition(M1,M2)
                return
            case 2.:
                M1 = get_matrix()
                M2 = get_matrix()
                result = matrix_subtraction(M1,M2)
                return
            case 3.:
                while(True):
                    M1 = get_matrix()
                    M2 = get_matrix()
                    if(len(M2)!=len(M1[0])):
                        print("количество столбцов первой матрицы не совпадает с кол-вом строк второй матрицы ,введите матрицы снова")
                        continue
                    matrix_multiplication(M1,M2)
                    return
            case _:
                print ("\nerror некорректный ввод error\n")

def get_matrix(matrix_number):
    while(True):
        rows = input(f"введите кол-во строк {matrix_number} матрицы:")
        try:
            float(rows)
        except:
            print ("\nerror некорректный ввод error\n")
            continue
        if (float(rows)!=int(rows)):
            print ("\nerror некорректный ввод error\n")
            continue
        else:
            rows = int(rows)
            break
    while (True):
        cols = input(f"введите кол-во столбцов {matrix_number} матрицы:")
        try:
            float(cols)
        except:
            print ("\nerror некорректный ввод error\n")
            continue
        if (float(cols)!=int(cols)):
            print ("\nerror некорректный ввод error\n")
            continue
        else:
            cols = int(cols)
            break
    print(f"введите матрицу размером {rows}x{cols} построчно через пробел:")

    result_matrix = []
    for row in range(rows):
        while(True):
            str_row = input(f"Строка {row+1}:")
            arr_str_row = str_row.split()
            if (not check_str(arr_str_row,cols)):
                continue
            arr_num_row = [float(num) for num in arr_str_row]
            result_matrix.append(arr_num_row)
            break
    return result_matrix      

def check_str(arr_str_row,cols):#проверяет строку на наличие в ней только float элементов через пробел
    for num in arr_str_row:
        print(f"{num} ")
        try:
            float(num)
        except:
            print ("\nerror некорректный ввод error\n")
            return False
    if (len(arr_str_row)!=cols):
        print ("\nerror некорректный ввод error\n")
        return False
    return True

def matrix_addition(matrix1,matrix2):
    result = []
    for row_index in range(len(matrix1)):
        row = [num1+num2 for num1,num2 in (matrix1[row_index],matrix2[row_index])]
        result.append(row)
    return result

def matrix_subtraction(matrix1,matrix2):
    result = []
    for row_index in range(len(matrix1)):
        row = [num1-num2 for num1,num2 in (matrix1[row_index],matrix2[row_index])]
        result.append(row)
    return result
    return

def matrix_multiplication(matrix1,matrix2):
    result = []
    for row in range(len(matrix1)):
        matrix_row =[]
        for col in range(len(matrix2[0])):
            element = 0
            for index in range(len(matrix2)):
                element+=matrix1[row][index]*matrix2[index][col]
            matrix_row.append(element)
        result.append(matrix_row)
    return result

def matrix_print(matrix):
    for i in matrix:
        st = ""
        for j in i:
            st += str(j)+' '
        print(st)
    return
