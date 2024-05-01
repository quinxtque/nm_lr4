
n = 4
m = 4
p = 1
rounder = 8
m_size = 4


def Mul(matrix1, matrix2):
    result = []

    for i in range(n):
        result.append([])
        for j in range(p):
            summ = 0
            for k in range(m):
                summ += matrix1[i][k] * matrix2[k]
            result[i].append(summ)

    return result


def Add(matrix1, matrix2):
    result = []
    for i in range(n):

        for j in range(p):
            result.append(matrix1[i][j] + matrix2[i])

    return result


def show_x(x):
    print("  ", end=' ')
    for i in range(len(x)):
        print(f"{i:>11}", end=' ')
    print()

    for i in range(len(x[0])):
        print(f"x{i + 1}", end=' ')
        for j in range(len(x)):
            #round(x[j][i], rounder)
            print(f"{x[j][i]:>11.8f}".replace('.', ','), end=' ')
        print()


def show_delta(d):
    print("d ", end=' ')
    for i in range(len(d)):
        #round(d[i], rounder)
        print(f"{d[i]:>11.8f}".replace('.', ','), end=' ')
    print()

'''
C = [
    [0, 0.2, -0.2],
    [-0.25, 0, 0.5],
    [-0.25, 0.25, 0]
]

d = [0.8, 0.5, 0.5]
'''

C = [
    [0, 0.020667, -0.004, -0.060667],
    [0.203252, 0, 0.081301, -0.073171],
    [0.2625, -0.125, 0, 0.1625],
    [-0.048889, -0.002222, 0.011667, 0]
]


d = [-0.058667, -0.739837, 3.2, 0.068889]

pre_q = []

for i in range(n):
    summ = 0
    for j in range(m):
        summ += abs(C[i][j])
    pre_q.append(summ)

q = max(pre_q)
print(q)

x = [d]
delta = [1]
e = 0.0005
k = 0

while True:
    if k != 0:
        delta.append(pow(q, k) / (1 - q) * max([abs(x[1][i] - x[0][i]) for i in range(m_size)]))

    if delta[k] <= e:
        break

    x.append(list(x[k]))

    for i in range(n):
        xn = []
        for j in range(m):
            xn.append(C[i][j] * x[k + 1][j])
            #print(f"[{i}] {C[i][j]} * {x[k + 1][j]} = {xn[j]}")

        xn.append(d[i])
        x[k + 1][i] = sum(xn)
        #print(f"{x[k + 1]}\n")

    #print(x)
    #exit()
    k += 1

show_x(x)
show_delta(delta)
