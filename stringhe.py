# Esercizio 1

testo = "Filippo"
print("Primo carattere:", testo[0])  # <Primo carattere: F>
print("Ultimo carattere:", testo[-1])  # <Ultimo carattere: o>

# Esercizio 2

testo = "AdOm"
print(testo.upper())  # <ADOM>
print(testo.lower())  # <adom>

# Esrcizio 3 

testo = "programmazione"
lettera = "a"
conteggio = testo.count(lettera)
print(f"La lettera '{lettera}' appare {conteggio} volte nella parola '{testo}'.")  #  <la lettera 'a' appare 2 volte nella parola 'programmazione'>

#Esercizio 4 
testo = "fantastico"
print(testo.startswith("f"))  # <True>
print(testo.endswith("o"))  # <True>

#Esercizio 5
testo = "Python"
print(testo[::-1])  # <nohtyP>

#Esercizio 6
testo = " Ciao mondo "
print(testo.strip())  # <Ciao mondo>

#Esercizio 7
parola = "programmazione"
print(parola[:3]*3)  # <propropro>
