def main():
    andmetöötlus()

def juurdekasv(pindala, aasta_juurdekasv):
    return round(pindala * 0.4047 * aasta_juurdekasv, 2)

def andmetöötlus():
    failinimi = input("Sisestage failinimi: ")
    kasutaja_juurdekasv = float(input("Sisestage aastane juurdekasv hektari kohta tihumeetrites: "))
    piir = float(input("Sisestage piir, mitmest aakrist suuremad metsatükid arvesse võtta: "))
    arvutatud = 0
    try:
        with open(failinimi, "r") as f:
            for rida in f:
                try:
                    pindala = float(rida.strip())
                    if pindala > piir:
                        arvutatud += 1
                        print(f"Metsatüki aastane juurdekasv on {juurdekasv(pindala, kasutaja_juurdekasv)}")
                    else:
                        print("Metsatükki ei võeta arvesse")
                except ValueError:
                    print("Invalid data in file:", rida)
            print(f"Arvutati {arvutatud} metsatüki juurdekasv")
    except FileNotFoundError:
        print("File not found:", failinimi)

if __name__ == "__main__":
    main()