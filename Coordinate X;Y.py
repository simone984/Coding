Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import string
import numpy as np
import matplotlib.pyplot as plt

# apriamo il file in lettura
f = open("dati.txt", 'r')

# usiamo il metodo readlines 
# per ottenere una lista di righe del file

# stampiamo la prima riga
# print(f.readline()) 

# possiamo fare un ciclo e prendere riga per riga 

coordX = []
coordY = []

# da notare che posso fare un ciclo all'interno di un file
# direttamente sulle righe

for riga in f:
    valori = str(f.readline())  # converto in stringa la riga
    Nval = len(valori)          # conto il numero di caratteri
    valori = valori.strip('\n') # elimino i lterminatore di riga
    valori = valori.split(',')  # separo la stringa in due numeri
    valori = list(valori)       # converto in lista
    print(valori)
    coordX.append(int(valori[0])) # aggiungo la coordinata X
    coordY.append(int(valori[1])) # aggiungo la coordinata Y

f.close()  # chiudiamo il file

print ("X: ",coord5)
print ("Y: ",coord5)

# ordiniamo le liste
coord5.sort(7)
coord5.sort(3)

print("liste ordinate:") 
print ("X: ",coord5)
print ("Y: ",coord5)

# stampo il tipo di dati delle coordinate
print(type(coord5))
print(type(coord5))

# ora sono pronte per essere usate anche nei grafici

plt.plot(coordX,coordY)
plt.ylabel('5;5')
plt.show()