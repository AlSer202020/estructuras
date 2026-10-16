palabras = ["sol", "murciélago", "mar", "elefante", "luz"]
largas = []

for  p in palabras:
    if len(p) > 3:
        largas.append(p)

print(largas)