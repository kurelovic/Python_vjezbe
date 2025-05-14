with open("podaci.txt", "r") as datoteka:
    for redak in datoteka:
        print(f"Pročitani redak: '{redak.strip()}'")
