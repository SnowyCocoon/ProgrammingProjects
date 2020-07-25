# -----------------------------------------------------------
# Autor: Dominik Strzałko (SnowyCocoon)
# Zadanie: 4 - Algorytm Prima (MSP)
# Data: 23.04.2020
# GitHub: https://github.com/SnowyCocoon
# Strona Internetowa: https://snowycocoon.com/
# Itch.io: https://snowycocoon.itch.io/
# -----------------------------------------------------------
def readfile(temp):
    f = open('graph07.txt')
    temp = [line.split() for line in f]
    for i in range (len(temp)):
      for j in range (len(temp)):
        if(temp[i][j] == "-"):
          temp[i][j] = float('inf')
        else:
          temp[i][j] = int(temp[i][j])

    f.close()
    return temp

def najmniejszy(temp, klucz, treeCheck):
  min = float('inf')

  for v in range(len(temp)):
    if(klucz[v] < min and treeCheck[v] == False):
      min = klucz[v]
      output = v
  
  return output

def prim(temp):
  klucz = [float('inf')] * len(temp)
  rodzic = [None] * len(temp)
  klucz[0] = 0
  treeCheck = [False] * len(temp)

  rodzic[0] = -1

  for x in range(len(temp)):
    u = najmniejszy(temp, klucz, treeCheck)
    print(f'Rozważamy wierzchołek: {u + 1}')
    treeCheck[u] = True
    for v in range(len(temp)):
      if klucz[v] > temp[u][v] and treeCheck[v] == False:
        klucz[v] = temp[u][v]
        rodzic[v] = u + 1
    for p in range(len(temp)):
      a = rodzic[p]
      print(f'[{a},{klucz[p]}]', end ="")
    print('')
  
  print('Krawedzie drzewa: ', end ="")
  for p in range(1, len(temp)):
    print(f'({p + 1},{rodzic[p]})', end ="")
  print('')

  suma = 0
  for p in range(len(temp)):
    suma += klucz[p]
  print(f'Waga drzewa: {suma}')


def main():
    neo = []
    neo = readfile(neo)

    prim(neo)

if __name__ == '__main__':
    main()