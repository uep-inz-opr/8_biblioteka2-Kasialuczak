class Biblioteka:
 dostepne_ksiazki=[]
 def __init__(self):
  self.ksiazka=dict()
 
 def dodaj_egzemplarz_ksiazki(self, tytul, autor, rok_wydania):
  self.dostepne_ksiazki.append(tytul)
  return True

class Czytelnik(Biblioteka):
 limit = 3
 wypozyczone_ksiazki=[]
 lista_wypozyczonych_ksiazek=[]
 oddane=[]
 def __init__(self):
  self.nazwisko=dict()
 def wypozycz(self, nazwisko,tytul):
  self.wypozyczone_ksiazki.append(nazwisko)
  self.lista_wypozyczonych_ksiazek.append((nazwisko,tytul))
  lista_nazwisk=set(self.wypozyczone_ksiazki)
  lista_nazwiska_tytul=set(self.lista_wypozyczonych_ksiazek)
  if tytul in self.dostepne_ksiazki:
   for l in lista_nazwisk:
    if (self.wypozyczone_ksiazki.count(l) <= self.limit):
     for m in lista_nazwiska_tytul:
      if self.lista_wypozyczonych_ksiazek.count(m)<2:
        self.dostepne_ksiazki.remove(tytul)
        return True
      else:
        self.wypozyczone_ksiazki.remove(l)
        self.lista_wypozyczonych_ksiazek.remove(m)
        return False
    else:
     self.wypozyczone_ksiazki.remove(l)
     self.lista_wypozyczonych_ksiazek.pop()
     return False
  else:
   self.wypozyczone_ksiazki.pop()
   self.lista_wypozyczonych_ksiazek.pop()
   return False

def oddaj(self, nazwisko, tytul):
 self.oddane.append((nazwisko,tytul))
 for n in self.oddane:
  if n in self.lista_wypozyczonych_ksiazek:
   self.wypozyczone_ksiazki.remove(nazwisko)
   self.lista_wypozyczonych_ksiazek.remove(n)
   self.oddane.remove(n)
   self.dostepne_ksiazki.append(tytul)
   
   return True
 else:
   return False

biblioteka = Biblioteka()
czytelnik = Czytelnik()
for i in range(int(input())):
 t = eval(input())
 if t[0] == "dodaj":
  print(biblioteka.dodaj_egzemplarz_ksiazki(t[1], t[2], t[3]))
 elif t[0] == "wypozycz":
  print(biblioteka.wypozycz(t[1],t[2]))
 elif t[0]=="oddaj":
  print(biblioteka.oddaj(t[1],t[2]))