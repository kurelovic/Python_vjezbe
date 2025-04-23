def broji_rijeci(recenica):
    broj=1
    for slovo in recenica:
        if slovo==" ":
            broj=broj+1
    return broj
broj=broji_rijeci("python jw r21")
print(broj)
