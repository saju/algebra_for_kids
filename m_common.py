import random

def gen_Nx_eq_M(N_max, M_max):
    N = random.randint(1, N_max+1)
    x = random.randint(1, M_max+1)
    M = N * x
    return (N, x, M)
