# -----------------------------------------------------------
# Autor: Dominik Strzałko (SnowyCocoon)
# Zadanie: ???
# Data: 23.03.2020
# GitHub: https://github.com/SnowyCocoon
# Strona Internetowa: https://snowycocoon.com/
# -----------------------------------------------------------
#Początek programu. Podajemy liczbę wierszy i kolumn.
rows = int(input('Podaj liczbę wierszy: '))
columns = int(input('Podaj liczbę kolumn: '))
print('Twoje wymiary macierzy to wiersze: %i, kolumny: %i \n' % (rows,columns))

#Tworzymy macierz i wpisujemy w nią swoje wartości.
print('Wpisz swoje wartości do macierzy. zaczynając od a(11) idąc wierszami')
Grid = [0] * rows
for i in range(rows):
    Grid[i] = [0] * columns

for i in range(rows):
  for j in range(columns):
    Grid[i][j] = int(input())


#Drukowanie początkowej macierzy.
print('Twoja Macierz wygląda w następujący sposób: ')
for i in range(rows):
  print (Grid[i])
print('\n')

#ten krótki kawałek kodu sprawdza czy jest więcej wieszy czy kolumn (potrzebne nam to w ustaleniu gdzie jest ostatni element o tym samym indeksie wiersza i kolumny.
if rows <= columns:
  licznik = rows
else:
  licznik = columns

rzad = 0

#Początek sprawdzania. Sprawdzamy po kolej wszystkie elemeny macierzy o takich samych indeksach wiersza i kolumny.
for i in range(licznik):

#na początku każdej pętli sprawdzamy czy element ten jest 1, 0 czy może czymś innym.

#Kiedy jest zerem jesteśmy zmuszeni do zamiany wierszy (kiedy jest to możliwe).
  if Grid[i][i] == 0:
    for m in range(i+1, rows):
      if Grid[i][i] == 0 and Grid[m][i] != 0:
        for n in range(columns):
          temp = Grid [m][n]
          Grid [m][n] = Grid [i][n]
          Grid [i][n] = temp
    
#ponownie sprawdzamy w przypadku kiedy nie da się wstawić innej liczby niż 0 na Grid(i,i) (cała kolumna zer). Wtedy przerywamy program ponieważ nie da się dalej działać na tej macierzy.
  if Grid[i][i] == 0:
    break

#Sprawdzamy najpierw czy element jest liczbą inną niż 1. Jeżeli jest to cały wiersz dzielimy przez tę liczbę (zmienna "dziel"). Następnie odejmujemy wierszami elementy macierzy by uzyskać 0 pod daną liczbą na przekątnej. "dziel2" to zmienna która mówi nam ile razy mamy odjąć wiersz od innego wiersza w celu uzyskania 0 pod Grid(i,i)
  if Grid[i][i] != 1:
    dziel = Grid[i][i]
    for j in range(licznik):
      Grid[i][j] /= dziel
  for k in range(i+1, rows):
    if Grid[k][i] != 0:
      dziel2 = Grid[k][i]
      for l in range (columns):
        Grid[k][l] -= Grid[i][l] * dziel2

  rzad += 1
   
  



#ponownie drukujemy macierz w celu sprawdzania. Podajemy również rząd macierzy. 
print('Twoja Macierz po zredukowaniu wygląda w następujący sposób: ')
for i in range(rows):
  print (Grid[i])
print('\nRząd macierzy jest równy: %i' % rzad)
print('\nWykonał: Dominik Strzałko')