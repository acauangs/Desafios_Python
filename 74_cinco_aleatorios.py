#crie um programa que gere 5 números aleatorios ente 1 - 10 em uma tupla;
from random import randint  

tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(tupla)