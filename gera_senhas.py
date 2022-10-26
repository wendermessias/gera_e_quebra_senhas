import string
from random import random, choice

valores =   string.ascii_letters #todas a letras
valores += string.digits #numeros de 0 a 9
valores += string.punctuation # caracteres especiasis 
tamanho = 10
senha = ""

for i in range(tamanho):
  senha += (choice(valores))

print(senha)

 