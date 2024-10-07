import random
random.seed(None)
m = int(input("Ingrese número de asignaturas: "))
n = int(input("Ingrese número de salas: "))
asignaturas = list(range(0, m))
A = [0] * m
agi = round(m * 0.65)
for i in range(agi):
    a = random.randint(0, len(asignaturas) - 1)
    A[asignaturas[a]] = 1
    del asignaturas[a]
asignaturas = list(range(0, m))
B = [0] * m
agi = m / 5
agi = round(agi)
for i in range(agi):
    a = random.randint(0, len(asignaturas) - 1)
    B[asignaturas[a]] = random.randint(6, 10)
    del asignaturas[a]
for i in range(agi, m):
    a = random.randint(0, len(asignaturas) - 1)
    B[asignaturas[a]] = random.randint(1, 5)
    del asignaturas[a]
C = []
for j in range(n):
    C.append(random.randint(20, 45))
D = []
for j in range(n):
    D.append(random.randint(10, 40))
s = ""
archivo = open("solucion.lp", 'w')
archivo.write("max: ")
for i in range(1, m + 1):
    for j in range(1, n + 1):
        for k in range(1, 8):
            for a in range(1, 6):
                s = " + "
                if i == j == k == a == 1:
                    s = ""
                archivo.write(s + str(B[i - 1] / (1 + A[i - 1])) + " x_" + str(i) + "_" + str(j) + "_" + str(k) + "_" + str(a))
archivo.write(";\n")
archivo.write("s.t.\n")
for j in range(1, n + 1):
    for k in range(1, 8):
        for a in range(1, 6):
            for i in range(1, m + 1):
                s = " + "
                if i == 1:
                    s = ""
                archivo.write(s + "x_" + str(i) + "_" + str(j) + "_" + str(k) + "_" + str(a))
            archivo.write(" <= 1;\n")
for i in range(1, m + 1):
    for j in range(1, n + 1):
        for k in range(1, 8):
            for a in range(1, 6):
                archivo.write("x_" + str(i) + "_" + str(j) + "_" + str(k) + "_" + str(a) + " <= u_" + str(k) + "_" + str(a) + ";\n")
for k in range(1, 8):
    for a in range(1, 6):
        s = " + "
        if k == a == 1:
            s = ""
        archivo.write(s + "u_" + str(k) + "_" + str(a))
archivo.write(" >= 14;\n")
for k in range(1, 8):
    for a in range(1, 6):
        s = " + "
        if k == a == 1:
            s = ""
        archivo.write(s + "u_" + str(k) + "_" + str(a))
archivo.write(" <= 28;\n")
for i in range(1, m + 1):
    for j in range(1, n + 1):
        for k in range(1, 8):
            for a in range(1, 6):
                s = " + "
                if k == a == 1:
                    s = ""
                archivo.write(s + str(B[i - 1]) + " x_" + str(i) + "_" + str(j) + "_" + str(k) + "_" + str(a))
            archivo.write(" <= 1 + " + str(A[i - 1]) + ";\n")
for i in range(1, m + 1):
    for k in range(1, 8):
        for a in range(1, 6):
            for j in range(1, n + 1):
                s = " + "
                if j == 1:
                    s = ""
                archivo.write(s + "x_" + str(i) + "_" + str(j) + "_" + str(k) + "_" + str(a))
            archivo.write(" <= 1;\n")
for i in range(1, m + 1):
    for j in range(1, n + 1):
        for k in range(2, 7):
            for a in range(1, 6):
                archivo.write("x_" + str(i) + "_" + str(j) + "_" + str(k) + "_" + str(a) + " <= " + "x_" + str(i) + "_" + str(j) + "_" + str(k + 1) + "_" + str(a) + " + x_" + str(i) + "_" + str(j) + "_" + str(k - 1) + "_" + str(a) + ";\n")
for i in range(1, m + 1):
    for j in range(1, n + 1):
        for k in range(1, 7):
            for a in range(1, 6):
                archivo.write(str(D[j - 1]) + " x_" + str(i) + "_" + str(j) + "_" + str(k) + "_" + str(a) + " <= " + str(C[j - 1]) + " x_" + str(i) + "_" + str(j) + "_" + str(k) + "_" + str(a) + ";\n")
for i in range(1, m + 1):
    for j in range(1, n + 1):
        for k in range(1, 7):
            for a in range(1, 6):
                archivo.write(str(B[i - 1]) + " x_" + str(i) + "_" + str(j) + "_" + str(k) + "_" + str(a) + " >= 6;\n")
archivo.write("bin ")
for i in range(1, m + 1):
    for j in range(1, n + 1):
        for k in range(1, 8):
            for a in range(1, 6):
                s = ","
                if i == j == k == a == 1:
                    s = ""
                archivo.write(s + "x_" + str(i) + "_" + str(j) + "_" + str(k) + "_" + str(a))
for k in range(1, 8):
    for a in range(1, 6):
        	archivo.write(",u_" + str(k) + "_" + str(a))
archivo.write(";\n")
archivo.write("end;\n")
archivo.close()
