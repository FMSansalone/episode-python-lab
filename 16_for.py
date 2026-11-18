# Esercizio 1 

for i in range(1, 11):
    print(i) # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# Esercizio 2

for i in range(2, 21, 2):
    print(i) # 2, 4, 6, 8, 10, 12, 14, 16, 18, 20

# Esercizio 3

parola = "Python"
for c in parola:
    print(c) # P, y, t, h, o, n

# Esercizio 4

somma = 0
for i in range(1, 101):
    somma += i
print("Somma =", somma) # Somma = 5050

# Esercizio 5

for i in range(1, 11):
    print(f"3 x {i} = {3*i}") # 3 x 1 = 3, 3 x 2 = 6, 3 x 3 = 9, 3 x 4 = 12, 3 x 5 = 15, 3 x 6 = 18, 3 x 7 = 21, 3 x 8 = 24, 3 x 9 = 27, 3 x 10 = 30

# Esercizio 6

n = 5
fattoriale = 1
for i in range(1, n+1):
    fattoriale *= i
print("Fattoriale =", fattoriale) # Fattoriale = 120

# Esercizio 7 

parola = "programmazione"
vocali = "aeiou"
conta = 0
for c in parola:
    if c in vocali:
        conta += 1
print("Numero di vocali:", conta) # Numero di vocali: 6

# Esercizio 8 

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j, end="  ")
    print() 
# 1 1  1 2  1 3  
# 2 1  2 2  2 3  
# 3 1  3 2  3 3  

# Esercizio 9

for i in range(1, 11):
    if i == 5:
        continue
    print(i) # 1, 2, 3, 4, 6, 7, 8, 9, 10

# Esercizio 10

for i in range(1, 11):
    if i == 7:
        break
    print(i) # 1, 2, 3, 4, 5, 6