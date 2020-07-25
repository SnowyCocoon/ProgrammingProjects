# -----------------------------------------------------------
# Autor: Dominik Strzałko (SnowyCocoon)
# Zadanie: 2 - Krawędzie cięcia
# Data: 08.04.2020
# GitHub: https://github.com/SnowyCocoon
# Strona Internetowa: https://snowycocoon.com/
# Itch.io: https://snowycocoon.itch.io/
# -----------------------------------------------------------

import copy

class Macierz:
  matrix = []

def readfile():
    temp = Macierz()
    f = open('graph03.txt')

    temp.matrix = [line.split() for line in f]

    for i in range (len(temp.matrix)):
      for j in range (len(temp.matrix)):
        if(temp.matrix[i][j] == "-"):
          temp.matrix[i][j] = float('inf')

    f.close()
    return temp

def nastepnicy(temp):
  slownik = {}
  for i in range (len(temp.matrix)):
    lista = []
    for j in range (len(temp.matrix)):
      if(temp.matrix[i][j] != float('inf')):
        lista += [j+1]
    slownik[i+1] = lista
  return(slownik)

def UzupelnikKrawedzie(temp):
  lista = []
  for x, xy_list in temp.items():
    for y in xy_list:
        if (tuple((y,x)) not in lista):
            lista.append(tuple((x,y)))
  return(lista)


def usun(x,y, Nast_Slownik):
    temp =  copy.deepcopy(Nast_Slownik)
    if x in temp[y]:
        temp[y].remove(x)
    if y in temp[x]:
        temp[x].remove(y)
    return temp

def bfs(graph, root):
  visited, queue = [root], [root]

  while queue:
    s = queue.pop(0) 
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
        
  return visited


def CzyJestKrawedziaCiecia(krawedzie, Nast_Slownik):
    for krawedz in krawedzie:
        Nast_Slownik_minus_krawedz = usun(krawedz[0],krawedz[1],Nast_Slownik)
        visited = bfs(Nast_Slownik_minus_krawedz,int(krawedz[0]))
        if int(krawedz[1]) in visited:
            print(f'({krawedz[0]}, {krawedz[1]}) NIE')
        else:
            print(f'({krawedz[0]}, {krawedz[1]}) TAK')



def main():
    neo = Macierz()
    neo = readfile()
    krawedzie = []
    Nast_Slownik = {}

    
    Nast_Slownik = nastepnicy(neo)
    krawedzie = UzupelnikKrawedzie(Nast_Slownik)

    CzyJestKrawedziaCiecia(krawedzie, Nast_Slownik)



if __name__ == '__main__':
    main()