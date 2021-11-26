import random
import m_common

#
# python3 Nx_eq_M_simple.y
#
# Generates 10 questions of the form Nx = M, where both N & M are small numbers, the child
# has to solve for "x"
# 
# How I use this program..
# python3 Nx_eq_M_simple.py > qns_plus_answers.txt
# cat qns_plus_answers.txt | grep -v answer > qns.txt
# ... then printout qns.txt and hand over to the child :)
#

N_MAX = 5
M_MAX = 10

def gen_simple_mult(num_questions):
    for i in range(num_questions):
        (N, x, M) = m_common.gen_Nx_eq_M(N_MAX, M_MAX)
        print("Question %d" % i)
        print("%dx = %d" % (N, N * x))
        print("x = ?")
        print("answer %d" % x)
        print("**************************")

def parse_arguments():
    pass

if __name__ == "__main__":
    parse_arguments()
    gen_simple_mult(num_questions = 10)
