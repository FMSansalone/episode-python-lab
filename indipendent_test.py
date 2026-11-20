from abc import ABC, abstractmethod

class Prodotto(ABC):
    def __init__(self, nome, prezzo, quantità):
        self._nome = nome
        self._prezzo = prezzo
        self._quantità = quantità

    @property
    def nome(self):
        return self._nome

    @property
    def prezzo(self):
        return self._prezzo

    @property
    def quantità(self):
        return self._quantità

    @staticmethod
    def valida_quantità(quantità):
        if quantità <= 0:
            raise ValueError("La quantità non può essere negativa.")

    def rifornisci(self, quantità):
        self.valida_quantità(quantità)
        self._quantità += quantità
        print(f"Rifornimento effettuato: {quantità} unità aggiunte. Quantità attuale: {self._quantità}")

    def vendi (self, quantità):
        self.valida_quantità(quantità)
        if quantità > self._quantità:
            raise ValueError("Quantità insufficiente in magazzino.")
        self._quantità -= quantità
        print(f"Vendita effettuata: {quantità} unità vendute. Quantità attuale: {self._quantità}")

    @abstractmethod
    def descrizione(self):
        pass

    def __str__(self):
        return self.descrizione()
    def __add__(self, other):
        if isinstance(other, Prodotto):
            return self.prezzo + other.prezzo
        raise TypeError("L'operazione è supportata solo tra prodotti.")
    
class ProdottoAlimentare(Prodotto):
    def __init__(self, nome, prezzo, quantità, data_scadenza):
        super().__init__(nome, prezzo, quantità)
        self._data_scadenza = data_scadenza

    @property
    def data_scadenza(self):
        return self._data_scadenza

    def descrizione(self):
        return f"Prodotto Alimentare: {self.nome}, Prezzo: {self.prezzo:.2f}, Quantità: {self.quantità}, Data di Scadenza: {self.data_scadenza}"

class ProdottoElettronico(Prodotto):
    def __init__(self, nome, prezzo, quantità, garanzia):
        super().__init__(nome, prezzo, quantità)
        self._garanzia = garanzia

    @property
    def garanzia(self):
        return self._garanzia

    def descrizione(self):
        return f"Prodotto Elettronico: {self.nome}, Prezzo: {self.prezzo:.2f}, Quantità: {self.quantità}, Garanzia: {self.garanzia} anni"

if __name__ == "__main__":
    mela = ProdottoAlimentare("Mela", 0.5, 100, "30/11/2026")
    tv = ProdottoElettronico("TV", 499, 5, 2)
    print(mela)
    print(tv)
    mela.vendi(20)
    tv.rifornisci(3)
    print(tv + tv)