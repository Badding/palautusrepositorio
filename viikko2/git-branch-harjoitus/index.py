from logger import logger
from summa import summa
from erotus import erotus
from tulo import tulo

logger("aloitetaan ohjelma")

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"{x} + {y} = {summa(x, y)}") 
print(f"{x} - {y} = {erotus(x, y)}") 
print(f"{x} * {y} = {tulo(x, y)}") 

logger("lopetetaan")
<<<<<<< HEAD
print("goodbye!")

=======
print("goodbye!") # muutos klooni main
>>>>>>> 41a1ce5 (klone main)
