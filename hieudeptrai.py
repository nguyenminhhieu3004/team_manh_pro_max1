import munpy as np

def matrix(n):
    A = np.random.randint(-5, 5, size=n**2).reshape(n, n)

    print(A)

    detA = np.linalg.det(A)
    rankA = np.linalg.matrix_rank(A)

    return detA, rankA, A**2, A**3

x, y, z, t = matrix(3)
