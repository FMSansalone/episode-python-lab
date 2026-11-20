class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - €{self.price:.2f}"

    def __eq__ (self, other):
        if isinstance(other, Product):
             return self.name == other.name and self.price == other.price
        else: 
             return False

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_items(self, product):
        self.items.append(product)

    def remove_items(self, product):
        if product in self.items:
            self.items.remove(product)

    def total_price(self):
         return sum(item.price for item in self.items)

    def __len__(self):
         return len(self.items)

    def __str__(self):
        if not self.items:
            return "Il carrello è vuoto"
        else:
            righe = "\n".join(f"- {item}" for item in self.items)
            return f"Carrello:\n{righe}\nTotale: €{self.total_price():.2f}" 

    def __add__(self, other):
        nuovo = ShoppingCart()
        nuovo.items = self.items + other.items 
        return nuovo 

def new_func(cart1, cart2):
    unito = cart1 + cart2
    return unito

if __name__ == "__main__":
    penna = Product ("Penna", 1.50)
    quaderno = Product ("Quaderno", 1.00)
    zaino = Product ("Zaino", 30.00)

    cart1 = ShoppingCart()
    cart2 = ShoppingCart()

    cart1.add_items(penna)
    cart1.add_items(quaderno)
    cart2.add_items(zaino)

    print(cart1)
    print(cart2)

    unito = cart1 + cart2 
    print(unito)

    cart1.remove_items(penna)
    print(cart1)
    print("Articoli nel carello unito:", len(unito))

# Carrello:
# - Penna - €1.50
# - Quaderno - €1.00
# Totale: €2.50
# Carrello:
# - Zaino - €30.00
# Totale: €30.00
# Carrello:
# - Penna - €1.50
# - Quaderno - €1.00
# - Zaino - €30.00
# Totale: €32.50
# Articoli nel carello unito: 3
# Carrello:
# - Carrello - €1.00
# Totale: €1.00 
