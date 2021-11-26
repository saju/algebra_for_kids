import random

#
# python2 harder_multiplication.py
#
# Generates 10 questions of the form Ny = M, where both N & M are (slighly) bigger numbers.
# 
# How I use this program..
# python2 harder_multiplication.py > qns_plus_answers.txt
# cat qns_plus_answers.txt | grep -v answer > qns.txt
# ... then printout qns.txt and hand over to the child :)
#

MAX_N = 10
MAX_M = 30

def gen_simple_mult(num_questions):
    for i in range(num_questions):
        mult = random.randint(1, MAX_N + 1)
        y = random.randint(1, MAX_M + 1)
        print "Question %d" % i
        print "%dy = %d" % (mult, mult * y)
        print "y = ?"
        print "answer %d" % y
        print "**************************"

def parse_arguments():
    pass

if __name__ == "__main__":
    parse_arguments()
    gen_simple_mult(num_questions = 10)
