with open("podaci.txt", "a") as datoteka:
    datoteka.write("Ovo je prvi redak koji se upisuje.\n")
    datoteka.write("4.\n")
with open("podaci.txt", "r") as datoteka:
    sadrzaj = datoteka.read()
    print(sadrzaj)
