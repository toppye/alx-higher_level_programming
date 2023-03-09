0x02. Python - import & modules
0-add.py



#!/usr/bin/python3


if __name__ == "__main__":

    """Print the sum of 1 and 2."""

    from add_0 import add


    a = 1

    b = 2

    print("{} + {} = {}".format(a, b, add(a, b)))




=========================


1-calculation.py



#!/usr/bin/python3


if __name__ == "__main__":

    """Print the sum, difference, multiple and quotient of 10 and 5."""

    from calculator_1 import add, sub, mul, div


    a = 10

    b = 5


    print("{} + {} = {}".format(a, b, add(a, b)))

    print("{} - {} = {}".format(a, b, sub(a, b)))

    print("{} * {} = {}".format(a, b, mul(a, b)))

    print("{} / {} = {}".format(a, b, div(a, b)))




======================================


100-my_calculator.py



#!/usr/bin/python3


if __name__ == "__main__":

    """Handle basic arithmetic operations."""

    from calculator_1 import add, sub, mul, div

    import sys


    if len(sys.argv) - 1 != 3:

        print("Usage: ./100-my_calculator.py <a> <operator> <b>")

        sys.exit(1)


    ops = {"+": add, "-": sub, "*": mul, "/": div}

    if sys.argv[2] not in list(ops.keys()):

        print("Unknown operator. Available operators: +, -, * and /")

        sys.exit(1)


    a = int(sys.argv[1])

    b = int(sys.argv[3])

    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))




============================================

101-easy_print.py



#!/usr/bin/python3

__import__("os").write(1, "#pythoniscool\n".encode("UTF-8"))




============================================


102-magic_calculation.py



#!/usr/bin/python3



def magic_calculation(a, b):

    """Match bytecode provided by Holberton School."""

    from magic_calculation_102 import add, sub


    if a < b:

        c = add(a, b)

        for i in range(4, 6):

            c = add(c, i)

        return (c)


    else:

        return(sub(a, b))



==============================================


103-fast_alphabet.py



#!/usr/bin/python3

import string

print(string.ascii_uppercase)




==============================================


2-args.py



#!/usr/bin/python3


if __name__ == "__main__":

    """Print the number of and list of arguments."""

    import sys


    count = len(sys.argv) - 1

    if count == 0:

        print("0 arguments.")

    elif count == 1:

        print("1 argument:")

    else:

        print("{} arguments:".format(count))

    for i in range(count):

        print("{}: {}".format(i + 1, sys.argv[i + 1]))


