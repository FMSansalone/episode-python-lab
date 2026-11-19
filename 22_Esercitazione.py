# Esercizio 1

tuples = [(1, 3), (2, 1), (5, 0)]
ordinata = sorted(tuples, key=lambda x: x[1])
print("Ordinata:", ordinata) # Ordinata: [(5, 0), (2, 1), (1, 3)]

# Esercizio 2

t = (1, 2, 3, 4, 5, 6)
pari = tuple([x for x in t if x % 2 == 0])
print("Numeri pari:", pari) # Numeri pari: (2, 4, 6)

# Esercizio 3

t = (1, 2, 3, 4)
invertita = tuple(reversed(t))
print("Invertita:", invertita) # Invertita: (4, 3, 2, 1)

# Esercizio 4

s = "programmazione"
t = tuple(set(s))
print("Tupla caratteri unici:", t) # Tupla caratteri unici: ('n', 'o', 'm', 'g', 'a', 'z', 'i', 'e', 'p', 'r')

# Esercizio 5

a = [1, 2, 3]
b = ["a", "b", "c"]
zipped = list(zip(a, b))
print("Zip:", zipped) # Zip: [(1, 'a'), (2, 'b'), (3, 'c')]

# Esercizio 6

A = {1, 2, 3}
B = {3, 4, 5}
C = {5, 6}
diff = A ^ B ^ C
print("Diff simmetrica:", diff) # Diff simmetrica: {1, 2, 4, 6}
 
# Esercizio 7

frase = "ciao come stai ciao tutto bene"
uniche = set(frase.split())
print("Parole uniche:", uniche) # Parole uniche: {'stai', 'bene', 'come', 'tutto', 'ciao'}

# Esercizio 8

liste = [[1, 2, 3], [3, 4, 5], [6, 7]]
unione = set().union(*map(set, liste))
print("Unione:", unione) # Unione: {1, 2, 3, 4, 5, 6, 7}
