def Addition(Matrix1, Matrix2):
    x1 = len(Matrix1)
    y1 = len(Matrix1[0])
    x2 = len(Matrix2)
    y2 = len(Matrix2[0])
    if x1 != x2 or y1 != y2:
        print(0, file=fout)
        exit(0)
    Result_Matrix = []
    for i in range(x1):
        Result_Matrix.append([0] * y1)
    for i in range(x1):
        for j in range(y1):
            Result_Matrix[i][j] = Matrix1[i][j] + Matrix2[i][j]
    return Result_Matrix


def Subtraction(Matrix1, Matrix2):
    x1 = len(Matrix1)
    y1 = len(Matrix1[0])
    x2 = len(Matrix2)
    y2 = len(Matrix2[0])
    if x1 != x2 or y1 != y2:
        print(0, file=fout)
        exit(0)
    if x1 != x2 or y1 != y2:
        return "Error"
    Result_Matrix = []
    for i in range(x1):
        Result_Matrix.append([0] * y1)
    for i in range(x1):
        for j in range(y1):
            Result_Matrix[i][j] = Matrix1[i][j] - Matrix2[i][j]
    return Result_Matrix


def Multiply_two_matrix(Matrix1, Matrix2):
    x1 = len(Matrix1)
    y1 = len(Matrix1[0])
    x2 = len(Matrix2)
    y2 = len(Matrix2[0])
    if y1 != x2:
        print(0, file=fout)
        exit(0)
    Result_Matrix = []
    for i in range(x1):
        Result_Matrix.append([0] * y2)
    k = 0
    s = 0
    for i in range(x1 * y2):
        sum = 0
        for j in range(y1):
            sum += Matrix1[s][j] * Matrix2[j][k]
        Result_Matrix[s][i % y2] = sum
        k += 1
        if k == y2:
            s += 1
            k = 0
    return Result_Matrix


def Multiply_by_number(Matrix, number):
    x = len(Matrix)
    y = len(Matrix[0])
    for i in range(x):
        for j in range(y):
            Matrix[i][j] = number * Matrix[i][j]
    return Matrix


def Transposition(Matrix):
    x = len(Matrix)
    y = len(Matrix[0])
    Matrix = [list(x) for x in zip(*Matrix)]
    return Matrix


def Result(Matrix_A, Matrix_B, Matrix_C, Matrix_D, Matrix_F, a, b):
    Result_Matrix = []
    Result_Matrix = Subtraction(Multiply_two_matrix(Multiply_two_matrix(Matrix_C, Transposition(Addition(Multiply_by_number(Matrix_A, a),Multiply_by_number(Transposition(Matrix_B), b)))), Matrix_D), Matrix_F)
    return Result_Matrix

fin = open("input.txt")
fout = open("output.txt", "w")
Input_Array = list(map(float, fin.readline().rstrip().split()))
a, b = Input_Array[0], Input_Array[1]
Input_Array = list(map(int, fin.readline().rstrip().split()))
nA, mA = Input_Array[0], Input_Array[1]
Input_Array = list(map(float, fin.readline().rstrip().split()))
Matrix_A = []
for i in range(nA):
    Matrix_A.append([0] * mA)
k = 0
for i in range(len(Input_Array)):
    Matrix_A[k][i % mA] = Input_Array[i]
    if i % mA == mA - 1:
        k += 1
Input_Array = list(map(int, fin.readline().rstrip().split()))
nB, mB = Input_Array[0], Input_Array[1]
Input_Array = list(map(float, fin.readline().rstrip().split()))
Matrix_B = []
for i in range(nB):
    Matrix_B.append([0] * mB)
k = 0
for i in range(len(Input_Array)):
    Matrix_B[k][i % mB] = Input_Array[i]
    if i % mB == mB - 1:
        k += 1
Input_Array = list(map(int, fin.readline().rstrip().split()))
nC, mC = Input_Array[0], Input_Array[1]
Input_Array = list(map(float, fin.readline().rstrip().split()))
Matrix_C = []
for i in range(nC):
    Matrix_C.append([0] * mC)
k = 0
for i in range(len(Input_Array)):
    Matrix_C[k][i % mC] = Input_Array[i]
    if i % mC == mC - 1:
        k += 1
Input_Array = list(map(int, fin.readline().rstrip().split()))
nD, mD = Input_Array[0], Input_Array[1]
Input_Array = list(map(float, fin.readline().rstrip().split()))
Matrix_D = []
for i in range(nD):
    Matrix_D.append([0] * mD)
k = 0
for i in range(len(Input_Array)):
    Matrix_D[k][i % mD] = Input_Array[i]
    if i % mD == mD - 1:
        k += 1
Input_Array = list(map(int, fin.readline().rstrip().split()))
nF, mF = Input_Array[0], Input_Array[1]
Input_Array = list(map(float, fin.readline().rstrip().split()))
Matrix_F = []
for i in range(nF):
    Matrix_F.append([0] * mF)
k = 0
for i in range(len(Input_Array)):
    Matrix_F[k][i % mF] = Input_Array[i]
    if i % mF == mF - 1:
        k += 1
Result = Result(Matrix_A, Matrix_B, Matrix_C, Matrix_D, Matrix_F, a, b)
print(1, file=fout)
print(len(Result), len(Result[0]), file=fout)
for i in range(len(Result)):
    for j in range(len(Result[0])):
        if Result[i][j].is_integer():
            Result[i][j] = int(Result[i][j])

for i in range(len(Result)):
    for j in range(len(Result[0])):
        fout.write(str(Result[i][j]))
        fout.write(" ")
    fout.write('\n')