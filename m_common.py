import random

#
# generate Nx = M
#
def gen_Nx_eq_M(N_max, X_max):
    N = random.randint(1, N_max+1)
    x = random.randint(1, X_max+1)
    M = N * x
    return (N, x, M)

def gen_Nx_plus_K_eq_M(N_max, X_max, K_max):
    N = random.randint(1, N_max+1)
    x = random.randint(1, X_max+1)
    K = random.randint(1, K_max+1)
    M = N*x + K
    return (N, x, K, M)
