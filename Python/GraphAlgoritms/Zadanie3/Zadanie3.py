# -----------------------------------------------------------
# Autor: Dominik Strzałko (SnowyCocoon)
# Zadanie: 3 - Algorytm Floyda-Warshalla 
# Data: 15.04.2020
# GitHub: https://github.com/SnowyCocoon
# Strona Internetowa: https://snowycocoon.com/
# Itch.io: https://snowycocoon.itch.io/
# -----------------------------------------------------------
import copy

class Macierz:
  matrix = []
  popMatrix = []
  najkrotsze = []

def readfile():
    temp = Macierz()
    f = open('graph05.txt')
    temp.matrix = [line.split() for line in f]
    for i in range (len(temp.matrix)):
      for j in range (len(temp.matrix)):
        if(temp.matrix[i][j] == "-"):
          temp.matrix[i][j] = float('inf')
        else:
          temp.matrix[i][j] = int(temp.matrix[i][j])

    temp.popMatrix = copy.deepcopy(temp.matrix)
    temp.najkrotsze = copy.deepcopy(temp.matrix)

    for i in range (len(temp.matrix)):
      for j in range (len(temp.matrix)):
        if(temp.najkrotsze[i][j] == float('inf')):
          temp.najkrotsze[i][j] = [0,0]
        else:
          temp.najkrotsze[i][j] = [i + 1,j + 1]

    for i in range (len(temp.matrix)):
      for j in range (len(temp.matrix)):
        if(temp.popMatrix[i][j] == float('inf')):
          temp.popMatrix[i][j] = None
        else:
          temp.popMatrix[i][j] = i+1

    f.close()
    return temp


def mayweather(temp):
  for k in range(len(temp.matrix)):
    for i in range(len(temp.matrix)):
      for j in range(len(temp.matrix)):
        if (temp.matrix[k][j] + temp.matrix[i][k] < temp.matrix[i][j]):
          temp.matrix[i][j] = temp.matrix[k][j] + temp.matrix[i][k]
          temp.popMatrix[i][j] = k + 1
          temp.najkrotsze[i][j][1] = temp.najkrotsze[k][j]
          temp.najkrotsze[i][j][0] = temp.najkrotsze[i][k] 
    print(f'W{k+1} = {temp.matrix}')
    print(f'p{k+1} = {temp.popMatrix} \n')

    for b in range(len(temp.matrix)):
      if(temp.matrix[b][b] < 0):
        print('Ujemny cykl. Nie ma rozwi¡zania')
        return False
        

  for i in range(5):
    if(temp.najkrotsze[1][i] != [0,0]):
      print(f'dla 1 do {i+1} = {temp.najkrotsze[0][i][0]}, {temp.najkrotsze[0][i][1]} \n')


def main():
    neo = Macierz()
    neo = readfile()

    print(f'W0 = {neo.matrix}')
    print(f'p0 = {neo.popMatrix} \n')  

    mayweather(neo)

if __name__ == '__main__':
    main()
