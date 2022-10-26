import sys
import string
from itertools import combinations_with_replacement
import time
from datetime import timedelta
from random import seed, random

def main(args):

  valores = string.ascii_letters
  valores += string.digits
  valores += string.punctuation
  tamanho = 6

  ini_t = time.time()
  gerar_senhas(valores, tamanho)
  fin_t = time.time()

  print("Tempo: " + str(fin_t - ini_t) + "s")

def gerar_senhas(valores, tamanho):
  comb = combinations_with_replacement(valores, tamanho)
  print ("Combinacoes: " + str(len(list(comb))))

if __name__ == '__main__':
    main(sys.argv[1:])
