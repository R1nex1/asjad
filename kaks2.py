import sys

def main():
    try:
        sõnastik = loe_seis("punktid.txt")
    except FileNotFoundError:
        print("Faili 'punktid.txt' ei leitud.")
        sys.exit(1)
    except Exception as e:
        print(f"Tekkis viga faili lugemisel: {e}")
        sys.exit(1)

    while True:
        print("1 - Vaata punktitabelit")
        print("2 - Lisa tulemus")
        print("3 - Leia korvpalluri keskmine")
        print("4 - Leia parim")
        print("5 - Lõpeta prograammi töö")
        valik = input("Vali tegevus: ")

        if valik == "1":
            for nimi, punktid in sõnastik.items():
                punktid_str = ' '.join(str(x) for x in punktid)
                print(f"{nimi} {punktid_str}")

        elif valik == "2":
            nimi = input("Sisesta nimi: ")
            try:
                tulemus = int(input("Sisesta punktid: "))
            except ValueError:
                print("Punktid peavad olema numbriline väärtus.")
                continue
            sõnastik = lisa_tulemus(nimi, sõnastik, tulemus)

        elif valik == "3":
            nimi = input("Sisesta nimi: ")
            if nimi in sõnastik:
                print(f"Mängijal {nimi} keskmine skoor on {leia_keskmine(nimi, sõnastik)}")
            else:
                print("Sellist mängijat ei ole sõnastikus.")

        elif valik == "4":
            leia_parim(sõnastik)

        elif valik == "5":
            salvesta_lõpeta(sõnastik,  "punktid_uus.txt")
            break

        else:
            print("Tundmatu valik. Palun proovi uuesti.")


def salvesta_lõpeta(sõnastik, fail):
    try:
        with open(fail, "w") as f:
            for nimi, punktid in sõnastik.items():
                punktid_str = ' '.join(str(x) for x in punktid)
                f.write(f"{nimi} {punktid_str}\n")
            print("Faili salvestatud. Programm lõpetas töö.")
    except Exception as e:
        print(f"Faili kirjutamisel tekkis viga: {e}")


def loe_seis(failinimi):
    tulemused = {}
    try:
        with open(failinimi, "r") as f:
            for rida in f:
                osad = rida.strip().split()
                nimi = osad[0]
                punktid = []
                try:
                    for punkt in osad[1:]:
                        punktid.append(int(punkt))
                except ValueError:
                    print(f"Viga punktide teisendamisel numbriliseks: {punkt}")
                    continue
                tulemused[nimi] = punktid
    except FileNotFoundError:
        print(f"Faili {failinimi} ei leitud.")
        raise
    except Exception as e:
        print(f"Tekkis viga faili {failinimi} lugemisel: {e}")
        raise
    return tulemused


def lisa_tulemus(nimi, sõnastik, tulemus):
    if not isinstance(tulemus, int):
        print("Tulemus peab olema täisarv.")
        return sõnastik
    if nimi in sõnastik:
        sõnastik[nimi].append(tulemus)
        print(f"Tulemus lisatud!")
    else:
        print(f"Sellist korvpallurit ei ole sõnastikus.")
    return sõnastik


def leia_keskmine(nimi, sõnastik):
    if nimi not in sõnastik:
        print(f"Sellist korvpallurit ei ole sõnastikus.")
        return None
    return sum(sõnastik[nimi]) / len(sõnastik[nimi])


def leia_parim(sõnastik):
    if not sõnastik:
        print("Sõnastik on tühi, parimat ei saa leida.")
        return
    parim = 0
    nimi = ""
    for nimed in sõnastik:
        hetkeskoor = leia_keskmine(nimed, sõnastik)
        if hetkeskoor is not None and hetkeskoor > parim:
            parim = hetkeskoor
            nimi = nimed
    if nimi:
        print(f"Parim on {nimi} tulemusega {parim}")
    else:
        print("Parimat mängijat ei leitud.")


if __name__ == "__main__":
    main()