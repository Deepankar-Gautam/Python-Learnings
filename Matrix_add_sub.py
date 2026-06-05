# Addition and Subtraction on 2D list

rows = int (input ("Enter the number of rows : ")) 
column = int (input ("Enter the number of column : "))

A, B, C, D = [], [], [], []

print ("Enter matrix A")

for i in range (0, rows):
    temp = []
    for j in range (0, column):
        value = int (input (f"Enter your value for {i+1}{j+1} : "))
        temp.append (value)
    A.append (temp)

print ()
print ("Enter matrix B")

for i in range (0, rows):
    temp = []
    for j in range (0, column):
        value = int (input (f"Enter your value for {i+1}{j+1} : "))
        temp.append (value)
    B.append (temp)

for i in range (0, rows):
    add, sub = [], []
    for j in range (0, column):
        add.append (A[i][j] + B[i][j])
        sub.append (A[i][j] - B[i][j])
    C.append (add)
    D.append (sub)

print ("\nMatrix A")
for i in range (rows):
    print (A[i])

print ("\nMatrix B")
for i in range (rows):
    print (B[i])

print ("\nMatrix Addition")
for i in range (rows):
    print (C[i])

print ("\nMatrix Subtraction")
for i in range (rows):
    print (D[i])