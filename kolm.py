class Tont:
    def __init__(self, nimi, vanus, elukoht):
        self.nimi = nimi
        self.vanus = vanus
        self.elukoht = elukoht

    def kummita(self):
        print(f"{self.nimi} kummitab elukohas {self.elukoht}!")

    def __str__(self):
        return f"Nimi: {self.nimi}, vanus: {self.vanus}, elukoht: {self.elukoht}"

class Võlur(Tont):
    def nõiu(self, nõiutav):
        print(f"{self.nimi} pani nõiduse, millega sai pihta {nõiutav.nimi}.")

norbert = Tont("Norbert", 31, "Tartu")
harry = Võlur("Harry", 17, "Tartu")
snape = Võlur("Snape", 35, "Tartu")

print(norbert)
norbert.kummita()

print(harry)
print(snape)
harry.nõiu(snape)