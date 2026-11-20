# PART 1: Variables & data types.

titolo = "Il Signore degli Anelli"
copie = 5
prezzo_medio = 18.90
disponibile = True 

print(titolo, type(titolo)) # Il Signore degli Anelli <class 'str'>
print(copie, type(copie)) # 5 <class 'int'>
print(prezzo_medio, type(prezzo_medio)) # 18.9 <class 'float'>
print(disponibile, type(disponibile)) # True <class 'bool'>

# PART 2: Data structures.

libri = ["Il Signore degli Anelli", "1984", "Blue Ocean", "Bible", "Quran"]
copie_libri = {"Il Signore degli Anelli": 1, "1984": 2, "Blue Ocean": 3, "Bible": 4, "Quran": 5}
utenti = {"Mario", "Anna", "Jack", "Brian", "Filippo"}

print(libri) 
print(copie_libri)
print(utenti)

# PART 3A: class Libro

class Libro:
    def __init__(self, titolo, autore, anno, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili

    def info(self):
        return f"{self.titolo} - {self.autore}({self.anno}) - Copie: {self.copie_disponibili}"

#   PART 3B: class Utente.

class Utente:
    def __init__(self, nome, eta, id_utente):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente

    def scheda(self):
        print(f"Utente #{self.id_utente}: {self.nome}, {self.eta} anni")

# PART 3C: class Prestito.

class Prestito:
    def __init__(self, utente, libro, giorni):
        self.utente = utente
        self.libro = libro
        self.giorni = giorni

    def dettagli(self):
        print(f"{self.utente.nome} ha preso in prestito {self.libro.titolo} per {self.giorni} giorni")

# PART 4: The presta_libro function

def presta_libro(utente, libro, giorni):
    if  libro.copie_disponibili >=1:
        libro.copie_disponibili -=1
        prestito = Prestito(utente, libro, giorni)
        return prestito
    else:
        print(f"Nessuna copia disponibile di {libro.titolo}")
        return None

if __name__ == "__main__":
    # 1. Create 3 books
    libro1 = Libro("1984", "George Orwell", 1949, 2)
    libro2 = Libro("Blue Ocean", "Mr. X", 2004, 1)
    libro3 = Libro("Bible", "Jesus", 0, 3)

    # 2. Create 3 users
    u1 = Utente ("Mario", 30, 1)
    u2 = Utente ("Filippo", 28, 2)
    u3 = Utente ("Brian", 30, 3)

    # 3. Create loans & save them in a list
    prestiti = []
    p = presta_libro (u1,libro1, 14)
    if p:
        prestiti.append(p)
    p = presta_libro (u2, libro1, 14)
    if p: prestiti.append(p)
    p = presta_libro (u3, libro2, 10)
    if p: prestiti.append(p)
    p = presta_libro(u3, libro1, 7)
    if p:
        prestiti.append(p)

    # 4. Print updated copies
    print("\n=== Copie disponibili ===")
    for libro in [libro1, libro2, libro3]:
        print(libro.info())

    # 5. Print loan details
    print("\n=== Prestiti ===") 
    for p in prestiti:
        p.dettagli()

# === Copie disponibili ===
# 1984 - George Orwell(1949) - Copie: 0
# Blue Ocean - Mr. X(2004) - Copie: 0
# Bible - Jesus(0) - Copie: 3

# === Prestiti ===
# Mario ha preso in prestito 1984 per 14 giorni
# Filippo ha preso in prestito 1984 per 14 giorni
# Brian ha preso in prestito Blue Ocean per 10 giorni