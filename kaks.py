def main():
    tulemused = loe_seis("turniir.txt")
    
    while True:
        print("1 - Kuva kõik tulemused")
        print("2 - Lisa tulemus")
        print("3 - Leia osaleja skoor")
        print("4 - Leia suurima skooriga osaleja")
        print("5 - Salvesta ja lõpeta")
        valik = input("Vali tegevus: ")
        
        if valik == "1":
            for nimi, punktid in tulemused.items():
                punktid_str = ' '.join(str(x) if x is not None else '-' for x in punktid)
                print(f"{nimi} {punktid_str}")
        
        elif valik == "2":
            nimi = input("Sisesta osaleja nimi: ")
            voor = int(input("Sisesta vooru number: "))
            tulemus = int(input("Sisesta tulemus: "))
            tulemused = lisa_tulemus(nimi, voor, tulemused, tulemus)
        
        elif valik == "3":
            nimi = input("Sisesta osaleja nimi: ")
            skoor = leia_skoor(nimi, tulemused)
            print(f"{nimi} skoor on {skoor}")
        
        elif valik == "4":
            max_skoor = 0
            max_nimi = None
            for nimi in tulemused:
                skoor = leia_skoor(nimi, tulemused)
                if skoor > max_skoor:
                    max_skoor = skoor
                    max_nimi = nimi
            if max_nimi:
                print(f"Suurima skooriga on {max_nimi} ({max_skoor} punkti).")
        
        elif valik == "5":
            with open("turniir_uus.txt", "w") as f:
                for nimi, punktid in tulemused.items():
                    punktid_str = ' '.join(str(x) if x is not None else '-' for x in punktid)
                    f.write(f"{nimi} {punktid_str}\n")
            print("Andmed salvestatud faili 'turniir_uus.txt'. Programm lõpetab töö.")
            break
        
        else:
            print("Tundmatu valik. Palun proovi uuesti.")


def loe_seis(failinimi):
    tulemused = {}
    with open(failinimi, "r") as f:
        next(f)
        for rida in f:
            osad = rida.strip().split()
            nimi = osad[0]
            punktid = []
            for punkt in osad[1:]:
                if punkt == "-":
                    punktid.append("-") 
                else:
                    punktid.append(int(punkt))
            tulemused[nimi] = punktid
    return tulemused


def lisa_tulemus(nimi, voor, sõnastik, tulemus):
    if nimi in sõnastik:
        if voor - 1 < len(sõnastik[nimi]):
            if sõnastik[nimi][voor - 1] is "-": 
                sõnastik[nimi][voor - 1] = tulemus
                print(f"Tulemus lisatud!")
            else:
                print(f"Tulemus on juba varem lisatud.")
        else:
            print(f"Viga: {nimi} jaoks pole vooru {voor} olemas.")
    else:
        print(f"Viga: Osaleja {nimi} ei ole nimekirjas.")
    return sõnastik


def leia_skoor(nimi, sõnastik):
    skoor = 0
    if nimi in sõnastik:
        for tulemused in sõnastik[nimi]:
            if tulemused == "-":
                pass
            else:
                skoor += tulemused
    return skoor


if __name__ == "__main__":
    main()