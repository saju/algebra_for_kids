#
# generic ax + b = c equation generator.
#
# Check README for usage
#
#
import argparse
import random

A_MAX = 10
A_MIN = 1

B_MAX = 10
B_MIN = 1

X_MAX = 10
X_MIN = 1

NUM_QUESTIONS = 10


def gen_eqn(a_min, a_max, x_min, x_max, b_min, b_max):
    A = random.randint(a_min, a_max+1)
    x = random.randint(x_min, x_max+1)
    B = random.randint(b_min, b_max+1)

    C = A*x + B
    return (A, x, B, C)

def prettify_eqn(A, B, C):
    if B > 0:
        return "%dx + %d = %d" % (A, B, C)
    elif B == 0:
        return "%dx = %d" % (A, C)
    else:
        return "%dx - %d = %d" % (A, (B * -1), C)
    

def gen_eqns(args):
    for i in range(args.numQ):
        (A, x, B, C) = gen_eqn(args.minA, args.maxA, args.minX, args.maxX,
                               args.minB, args.maxB)
        print("Question %d" % i)
        print(prettify_eqn(A, B, C))
        print("x = ?")
        print("answer %d" % x)
        print("**************************")


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--maxA', type=int, required=False, default=A_MAX)
    parser.add_argument('--minA', type=int, required=False, default=A_MIN)
    parser.add_argument('--maxX', type=int, required=False, default=X_MAX)
    parser.add_argument('--minX', type=int, required=False, default=X_MIN)
    parser.add_argument('--maxB', type=int, required=False, default=B_MAX)
    parser.add_argument('--minB', type=int, required=False, default=B_MIN)
    parser.add_argument('--numQ', type=int, required=False, default=NUM_QUESTIONS)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_arguments()
    gen_eqns(args)

