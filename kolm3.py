class Sportlane:
    def __init__(self, nimi, kaal):
        self.nimi = nimi
        self.kaal = kaal


    def __str__(self):
        return f"Nimi: {self.nimi}, kaal: {self.kaal} kg."


class Maadleja(Sportlane):
    def __init__(self, nimi, kaal):
        super().__init__(nimi, kaal)
        self.kaaluklass = self.hinda_kaaluklass()

    def hinda_kaaluklass(self):
        if self.kaal <= 55:
            return "kärbeskaal"
        elif self.kaal <= 66:
            return "kergekaal"
        elif self.kaal <= 84:
            return "keskkaal"
        elif self.kaal <= 96:
            return "poolraskekaal"
        else:
            return "raskekaal"

    def muuda_kaalu(self, uus_kaal):
        self.kaal = uus_kaal
        self.kaaluklass = self.hinda_kaaluklass()

    def __str__(self):
        return f"Nimi: {self.nimi}, kaal: {self.kaal} kg, kaalukategooria: {self.kaaluklass}."
    

Indrek = Sportlane("Indrek", 105)
Georg = Maadleja("Georg", 83)
Kristjan = Maadleja("Kristjan", 115)
print(Indrek)
print(Georg)
print(Kristjan)

Kristjan.muuda_kaalu(95)
print(f"\n{Kristjan}")