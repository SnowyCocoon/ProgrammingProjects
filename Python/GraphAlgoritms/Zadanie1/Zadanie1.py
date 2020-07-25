# -----------------------------------------------------------
# Autor: Dominik Strzałko (SnowyCocoon)
# Zadanie: 1 - Odczytywanie/Zapisywanie
# Data: 23.03.2020
# GitHub: https://github.com/SnowyCocoon
# Strona Internetowa: https://snowycocoon.com/
# Itch.io: https://snowycocoon.itch.io/
# -----------------------------------------------------------

class Macierz:
  row_number = 0
  matrix = []
  zamiany = []

def readfile():
    temp = Macierz()
    f = open('graph.txt')
    temp.matrix = []
    
    temp.row_number = f.readline()
    for line in range(int(temp.row_number)):
        temp.matrix += [f.readline().split()]
    for line in f:
      temp.zamiany += [line.split()]

    for i in range (int(temp.row_number)):
      for j in range (int(temp.row_number)):
        if(temp.matrix[i][j] == "-"):
          temp.matrix[i][j] = float('inf')

    f.close()
    return temp

def nastepnicy(temp):
  slownik = {}
  for i in range (int(temp.row_number)):
    lista = []
    for j in range (int(temp.row_number)):
      if(temp.matrix[i][j] != float('inf')):
        lista += [j+1]
    slownik[i+1] = lista
  print(slownik)

def calyGrafzWagami(temp):
  slownik = {}
  for i in range (int(temp.row_number)):
    slownik2 = {}
    for j in range (int(temp.row_number)):
      if(temp.matrix[i][j] != float('inf')):
        slownik2[j+1] = temp.matrix[i][j]
    slownik[i+1] = slownik2
  print(slownik)

def listaKrawedzizWagami(temp):
  slownik = {}
  for i in range (int(temp.row_number)):
    for j in range (i,int(temp.row_number)):
      if(temp.matrix[i][j] != float('inf')):
        slownik[(i+1,j+1)] = temp.matrix[i][j]
  print(slownik)

def ladnaListaNastepnikow(temp):
  slownik = {}
  for i in range (int(temp.row_number)):
    lista = []
    for j in range (int(temp.row_number)):
      if(temp.matrix[i][j] != float('inf')):
        lista += [j+1]
    slownik[i+1] = lista
  print('Lista nastepnikow:')
  for i in slownik:
    print(i,' : ',slownik[i])

def usuIdod(temp):
  for i in temp.zamiany:
    if(temp.matrix[int(i[0])-1][int(i[1])-1] == float('inf')):
      temp.matrix[int(i[0])-1][int(i[1])-1] = 3
      temp.matrix[int(i[1])-1][int(i[0])-1] = 3
    else:
      temp.matrix[int(i[0])-1][int(i[1])-1] = float('inf')
      temp.matrix[int(i[1])-1][int(i[0])-1] = float('inf')
  return temp

def main():
    sebastian = Macierz()
    sebastian = readfile()
    nastepnicy(sebastian)
    print("")
    calyGrafzWagami(sebastian)
    print("")
    listaKrawedzizWagami(sebastian)
    print("")
    ladnaListaNastepnikow(sebastian)
    print("")
    print("")
    print("")
    print("Dodawanie i Usuwanie")
    print("")
    print("")
    sebastian = usuIdod(sebastian)
    print("")
    nastepnicy(sebastian)
    print("")
    calyGrafzWagami(sebastian)
    print("")
    listaKrawedzizWagami(sebastian)
    print("")
    ladnaListaNastepnikow(sebastian)


if __name__ == '__main__':
    main()
