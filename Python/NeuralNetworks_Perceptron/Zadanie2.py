# -----------------------------------------------------------
# Autor: Dominik Strzałko (SnowyCocoon)
# Zadanie: 2 - Perceptron
# Data: 23.03.2020
# GitHub: https://github.com/SnowyCocoon
# Strona Internetowa: https://snowycocoon.com/
# Itch.io: https://snowycocoon.itch.io/
# -----------------------------------------------------------

def FunkcjaAktywacji(input, weight, n):
  x = 0.0
  for i in range(n):
    x += (weight[i] * input[i])
  if x >= 0:
     return 1
  else:
     return 0




def Nauka(c, tablicaIn):
    wagi = [1.0] * 26
    t = 1
    licznik = 0

    while(licznik < 5):
      if (t % 5 + 1) <= 3:
        zt = 1
      else:
        zt = 0
      
      yt = FunkcjaAktywacji(tablicaIn[t%5], wagi, len(wagi))

      for i in range(26):
        #Serce
        wagi[i] = wagi[i] + c * (zt - yt) * tablicaIn[t % 5][i]
      t += 1
      if(zt == yt):
        licznik += 1
      else:
        licznik = 0
    print("\nDla C: " + str(c) + "\nT: " + str(t) + "\n")
    for i in range(len(wagi)):
        print("w" + str(i) + ":" + str(round(wagi[i], 5)))






def zamiana(tablicaIn):
  tablicaOut = []
  for i in range(26):
    if i in tablicaIn:
      tablicaOut.append(1.0)
    else:
      tablicaOut.append(0.0)
  return tablicaOut


def main():
  wejscia = []

  u1 = [6, 7, 12, 17, 22, 25]
  u2 = [2, 3, 8, 13, 25]
  u3 = [5, 6, 11, 16, 21, 25]
  u4 = [6, 7, 8, 11, 13, 16, 17, 18, 25]
  u5 = [10, 11, 12, 15, 17, 20, 21, 22, 25]
  
  wejscia.append(zamiana(u1))
  wejscia.append(zamiana(u2))
  wejscia.append(zamiana(u3))
  wejscia.append(zamiana(u4))
  wejscia.append(zamiana(u5))

  print(wejscia)

  for c in [0.001, 0.01, 0.1, 1.0]:
      Nauka(c, wejscia)



if __name__ == '__main__':
    main()