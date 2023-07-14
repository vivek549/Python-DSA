# Program to check if a number is prime or not

n = 4.2

# isinstance(n, int/float) check for datatype
# n.is_integer() check if float is an interger (decimal point value is zero

# function to check if number is interger (datatype is integer or a float is integer)
def is_integer_num(n):
    if isinstance(n, int):
        return True
    elif isinstance(n, float):
        return n.is_integer()


if n == 1 or is_integer_num(n) == False:
    print("neither prime nor composite")
    exit()

c = 2
# check if number is divisible be any number which is less than or equal to its square root
# checking through square root only, after that there will be repetitions (2 * 18 or 18 * 2)
while c*c <= n:
    if n % c == 0:
        print("composite")
        # exit program if we found type of number
        exit()
    c += 1
else:
    print("prime")