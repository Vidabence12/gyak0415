class Diak:
    def __init__(self, nev, osztaly, atlag):
        self.nev = nev
        self.osztaly = osztaly
        self.atlag = float(atlag)

diakok = []

fajl = open("diak.txt", "r", encoding="utf-8")

for sor in fajl:
    sor = sor.strip()
    reszek = sor.split(";")
    
    nev = reszek[0]
    osztaly = reszek[1]
    atlag = reszek[2]
    
    uj_diak = Diak(nev, osztaly, atlag)
    diakok.append(uj_diak)

fajl.close()

print("Létszám:", len(diakok))

osszeg = 0
for d in diakok:
    osszeg = osszeg + d.atlag

atlag = osszeg / len(diakok)
print("Csoportátlag:", round(atlag, 2))

legjobb = diakok[0]

for d in diakok:
    if d.atlag > legjobb.atlag:
        legjobb = d

print("Legjobb tanuló:", legjobb.nev, "-", legjobb.atlag)

van9 = False
van10 = False
van11 = False
van12 = False

for d in diakok:
    if d.osztaly[0] == "9":
        van9 = True
    if d.osztaly[0] == "1" and d.osztaly[1] == "0":
        van10 = True
    if d.osztaly[0] == "1" and d.osztaly[1] == "1":
        van11 = True
    if d.osztaly[0] == "1" and d.osztaly[1] == "2":
        van12 = True

print("Hiányzó évfolyam(ok):")

if not van9:
    print(9)
if not van10:
    print(10)
if not van11:
    print(11)
if not van12:
    print(12)