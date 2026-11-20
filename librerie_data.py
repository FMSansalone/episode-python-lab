# Crea un array con i numeri da 1 a 10, calcola i quadrati e i cubi, organizza i dati in un DataFrame e visualizza un grafico a linee.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

arr = np.arange(1,11)

quadrati = arr**2
cubi = arr**3

df = pd.DataFrame({

    "Numero": arr,
    "Quadrato": quadrati,
    "Cubo": cubi
    
})

print(df)

# Grafico

plt.plot(df["Numero"], df["Quadrato"], label = "Quadrati")
plt.plot(df["Numero"], df["Cubo"], label = "Cubi")
plt.xlabel("Numero")
plt.ylabel("Valore")
plt.title("Quadrati e Cubi")
plt.legend()
plt.show()

# risultato 

#    Numero  Quadrato  Cubo
# 0       1         1     1
# 1       2         4     8
# 2       3         9    27
# 3       4        16    64
# 4       5        25   125
# 5       6        36   216
# 6       7        49   343
# 7       8        64   512
# 8       9        81   729
# 9      10       100  1000
