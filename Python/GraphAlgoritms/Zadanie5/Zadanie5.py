# -----------------------------------------------------------
# Autor: Dominik Strzałko (SnowyCocoon)
# Zadanie: 5 - Cykle Hamiltona
# Data: 07.05.2020
# GitHub: https://github.com/SnowyCocoon
# Strona Internetowa: https://snowycocoon.com/
# Itch.io: https://snowycocoon.itch.io/
# -----------------------------------------------------------
def readfile(temp):
    f = open('graph09.txt')
    temp = [line.split() for line in f]
    for i in range (len(temp)):
      for j in range (len(temp)):
        if(temp[i][j] == "-"):
          temp[i][j] = float('inf')
        else:
          temp[i][j] = int(temp[i][j])

    f.close()
    return temp

def hamilton(matrix, stack, nodes):
  print(stack)
  if(len(stack)==len(matrix) and matrix[(stack[-1]) - 1][0] == 1):
    stack.append(stack[0])
    print("CYKL HAMILTONA: " + str(stack))
    stack.pop()
  for i in range(len(matrix)):
    if(matrix[stack[-1] - 1][i] == 1 and nodes <= 6 and (i+1) not in stack):
      hamilton(matrix,(stack + [i +1]), (nodes+1))
      print(stack)

def main():
    raxephon = []
    raxephon = readfile(raxephon)

    start = 1
    stack = [1]

    hamilton(raxephon,stack,start)

if __name__ == '__main__':
    main()