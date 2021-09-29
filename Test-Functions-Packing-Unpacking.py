
# Functions
def two_plus_two():
    val = 2 + 2
    return val

sum = (two_plus_two() * 2)
print(sum)

# print multiple numbers in functions
def multiply_two_nums(num1, num2):
    val = num1 * num2
    return val

print(multiply_two_nums(5, 10))


# Packing
def packer(*args):
    print(args)

packer("Hello", "I", "love", "python")

####
def calculate_total(*args):
    total = sum(args)
    print(total)

calculate_total(25, 25, 20, 30, 100)

def packer(*args):
    total = mul(args)
    print(total)

packer(5, 4, 3)

# Unpacking
first, last = input('Enter your full name: \n').split(' ')

print(first)
print(last)
