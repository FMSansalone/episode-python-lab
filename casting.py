# Esercizio 1

n_int = 4
n_float = float(n_int)
print(n_int, n_float)  # 4 4.0

# Esercizio 2

n_float = 9.8
n_int = int(n_float)
print(n_float, n_int)  # 9.8 9

# Esercizio 3

n_str = "456"
n_int = int(n_str)
print(n_str, n_int)  # "456" 456

# Esercizio 4

num_str = "6.78"
num_float = float(num_str)
print(num_float)  # 6.78

# Esercizio 5
n_str = "Hello"

try:
    num_int = int(n_str)

except ValueError:
    print("It is not possible to convert Hello(str) to int")


