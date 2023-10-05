
import numpy as np


runOnce=0
run=1

def get_matrix(dim):
    matrix = []
    print(f"Enter {dim}x{dim} matrix row by row each number seperated by a space:")
    for i in range(dim):
        row = list(map(float, input().split()))
        matrix.append(row)
    return np.array(matrix)

def add_matrices(matrix_a, matrix_b):
    return matrix_a + matrix_b

def subtract_matrices(matrix_a, matrix_b):
    return matrix_a - matrix_b

def multiply_matrices(matrix_a, matrix_b):
    return np.dot(matrix_a, matrix_b)

def transpose_matrix(matrix):
    return np.transpose(matrix)

def determinant(matrix):
    return np.linalg.det(matrix)

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def main():
    global run
    global runOnce
    global matrix_a
    global matrix_b
    global result
    global dim
    if runOnce == 0 :
        dim = int(input("Enter the dimension of the square matrices: "))
        print("Enter matrix A:")
        matrix_a = get_matrix(dim)
        print("Enter matrix B:")
        matrix_b = get_matrix(dim)
    
         

    print("\nSelect operation:")
    print("1. Add matrices")
    print("2. Subtract matrices")
    print("3. Multiply matrices")
    print("4. Transpose matrix A")
    print("5. Transpose matrix B")
    print("6. Determinant of matrix A")
    print("7. save result in matrix_a and input matrix_b" )
    print("8. reenter both matrix")
    print("9. exit")

    choice = int(input())

    if choice == 1:
        result = add_matrices(matrix_a, matrix_b)

    elif choice == 2:
        result = subtract_matrices(matrix_a, matrix_b)

    elif choice == 3:
        result = multiply_matrices(matrix_a, matrix_b)

    elif choice == 4:
        result = transpose_matrix(matrix_a)

    elif choice == 5:
        result = transpose_matrix(matrix_b)

    elif choice == 6:
        print("The determinant is",determinant(matrix_a) ) 

    elif choice == 7:
         matrix_a = result
         print("Enter matrix B:")
         matrix_b = get_matrix(dim)

    elif choice == 8:
        print("Enter new Matrix")

    elif choice == 9:
        run = 0
    else:
        print("Invalid choice!")
        return

    try:
        print("\nResult:")
        print_matrix(result)
    except NameError:
        pass

    if choice == 8:
        runOnce = 0
    else:
        runOnce = 1
    

    
while(run==1):
    
    main()
