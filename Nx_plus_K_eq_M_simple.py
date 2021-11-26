import random
import m_common

#
# python3 Nx_eq_M_simple.y
#
# Generates 10 questions of the form Nx + K = M, where N,x & K are small numbers, the child
# has to solve for "x"
# 
# How I use this program..
# python3 Nx_plus_K_eq_M_simple.py > qns_plus_answers.txt
# cat qns_plus_answers.txt | grep -v answer > qns.txt
# ... then printout qns.txt and hand over to the child :)
#

N_MAX = 5
X_MAX = 10
K_MAX = 10

def gen_eqns(num_questions):
    for i in range(num_questions):
        (N, x, K, M) = m_common.gen_Nx_plus_K_eq_M(N_MAX, X_MAX, K_MAX)
        print("Question %d" % i)
        print("%dx + %d = %d" % (N, K, M))
        print("x = ?")
        print("answer %d" % x)
        print("**************************")

def parse_arguments():
    pass

if __name__ == "__main__":
    parse_arguments()
    gen_eqns(num_questions = 10)
