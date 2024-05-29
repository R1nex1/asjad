def main():
    raamatud()


def raamatud():
    raamatud = input("Sisesta faili nimi: ").strip().lower()
    raamatu_aeg_kokku = 0
    try:
        with open(raamatud, "r") as r:
            for rida in r:
                try:
                    lk_arv = int(rida)
                    kirjastiil = input(f"Raamat on {lk_arv} lk. Kui suur on kirjastiil? ")
                    raamatu_aeg_kokku += lugemise_aeg(lk_arv, kirjastiil)
                except ValueError:
                        print("Failis on väär andmed:", rida)
            print(f"Kokku kulub raamatute lugemiseks {aeg_tundides(raamatu_aeg_kokku)}.")
    except FileNotFoundError:
        print("Faili ei leitud:", raamatud)


def lugemise_aeg(lk_arv, kirjasuurus):
    aeg = {"suur": 20, 
        "keskmine": 30, 
        "väike": 40}
    return int(lk_arv * aeg[kirjasuurus])


def aeg_tundides(aeg_sekundites):
    h = str((aeg_sekundites//3600))
    min = str((aeg_sekundites%3600)//60)
    sek = str((aeg_sekundites%3600)%60)
    return "{} tundi, {} minutit ja {} sekundit".format(h, min, sek)


if __name__ == "__main__":
    main()