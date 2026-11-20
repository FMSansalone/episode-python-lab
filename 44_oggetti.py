# Esercizio 1 - Calcolatrice

class Calcolatrice: 
    def dividi (self, a, b):
        try: 
            return a / b
        except ZeroDivisionError:
            print("Errore: divisione per zero non consentita.")
            return None

calc = Calcolatrice()
print(calc.dividi(10,2))
print(calc.dividi(10,0))

# 5.0
# Errore: divisione per zero non concentita.
# None


# Esercizio 2 - Persona

class Persona:
    def __init__(self, nome, eta):
        if eta < 0:
            raise ValueError ("L'età non può essere negativa!")
        self.nome = nome 
        self.eta = eta

try:
    p1 = Persona("Mario", 25)
    print("Persona creata:", p1.nome, p1.eta)
    p2 = Persona("Anna", -3)
except ValueError as e:
    print("Errore:", e) 

# Persona creata: Mario 25
# Errore: L'età non può essere negativa

# Esercizio 3 

class EtaNonValidaError(Exception):
    pass

class Studente:
    def __init__(self, nome, eta):
        if eta < 0 or eta > 120:
            raise EtaNonValidaError(f"Età non valida: {eta}")
        else:
            self.nome = nome
            self.eta = eta

try:
    s1 = Studente ("Luca", 20)
    print("Studente creato:", s1.nome, s1.eta)
    s2 = Studente ("Paolo", 150)
except EtaNonValidaError as e:
    print("Errore:", e)

# Studente creato: Luca 20
# Errore: Età non valida:150

            