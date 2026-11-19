# Esercizio 1

A = {"Anna", "Luca", "Marco"}
B = {"Luca", "Sara", "Marco"}
print("Entrambi:", A & B) # Entrambi: {'Marco', 'Luca'}
print("Solo A:", A - B) # Solo A: {'Anna'}
print("Totale unici:", len(A | B)) # Totale unici: 4

# Esercizio 2

A = {"Anna", "Luca", "Marco"}
B = {"Luca", "Sara", "Marco"}
print("Entrambi:", A & B) # Entrambi: {'Marco', 'Luca'}
print("Solo A:", A - B) # Solo A: {'Anna'} # Solo A: {'Anna'}
print("Totale unici:", len(A | B)) # Totale unici: 4

# Esercizio 3

import random
numeri = {random.randint(1, 20) for _ in range(10)}
print("Set casuale:", numeri) # Set casuale: {5, 6, 7, 8, 12, 13, 15, 16, 18}

#Esercizio 4

frase = "ciao come stai ciao tutto bene"
parole = frase.split()
conteggio = {}
for p in parole:
    conteggio[p] = conteggio.get(p, 0) + 1
print("Conteggio:", conteggio) # Conteggio: {'ciao': 2, 'come': 1, 'stai': 1, 'tutto': 1, 'bene': 1}

# Esercizio 5

d = {"a": 1, "b": 2, "c": 3}
inverso = {v: k for k, v in d.items()}
print("Inverso:", inverso) # Conteggio: {'ciao': 2, 'come': 1, 'stai': 1, 'tutto': 1, 'bene': 1}

# Esercizio 6

chiavi = ["nome", "età", "città"]
valori = ["Anna", 25, "Roma"]
d = dict(zip(chiavi, valori))
print("Dizionario:", d) # Dizionario: {'nome': 'Anna', 'età': 25, 'città': 'Roma'}

# Esercizio 7

parole = ["ciao", "come", "va", "oggi"]
gruppi = {}
for p in parole:
    gruppi.setdefault(len(p), []).append(p)
print("Raggruppate:", gruppi) # Raggruppate: {4: ['ciao', 'come', 'oggi'], 2: ['va']}

# Esercizio 8

testo = "programmazione"
freq = {}
for c in testo:
    freq[c] = freq.get(c, 0) + 1
print("Frequenza:", freq) # Frequenza: {'p': 1, 'r': 2, 'o': 2, 'g': 1, 'a': 2, 'm': 2, 'z': 1, 'i': 1, 'n': 1, 'e': 1}