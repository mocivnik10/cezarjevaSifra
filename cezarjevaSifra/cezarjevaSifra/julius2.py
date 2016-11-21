import string

def sifriranje():
    vnesen_tekst = raw_input('Prosim vnesi tekst: ').upper()
    # Lista vnesenih znakov - Zato da lahko dobimo index za vsak znak/crko posebej
    lista_vnesenih_znakov = list(vnesen_tekst)
    # V ta list se shranijo ze sifrirani vneseni znaki.
    sifrirana_lista = []

    for znak in lista_vnesenih_znakov:
        #Alphab je list vseh znakov Angleske abecede (Velike crke)
        alphab = list(string.ascii_uppercase)
        if znak == " ":
            # Presledek prepoznaj in ga prevedi kot presledek
            sifrirana_lista.append(" ")
        else:
            # Glede na index znaka v abecedi odstej -3 in dobil bos sifriran znak.
            _Dindex = alphab.index(znak) - 3
            # Dodaj sifriran znak v list sifrirana_lista
            sifrirana_lista.append(alphab[_Dindex])
    # zdruzi to listo v en string in jo izpisi v eni vrstici
    print ''.join(sifrirana_lista)

def desifriranje():
    vnesen_tekst = raw_input('Prosim vnesi sifriran tekst: ').upper()
    lista_vnesenih_znakov = list(vnesen_tekst)
    desifrirana_lista = []

    for znak in lista_vnesenih_znakov:
        alphab = list(string.ascii_uppercase)
        # Obrni abecedo - Reverse - Da lahko ciklicno odstejem -3 od indexov vnesenih znakov
        alphab = alphab[::-1]
        if znak == " ":
            desifrirana_lista.append(" ")
        else:
            _Dindex = alphab.index(znak) - 3
            desifrirana_lista.append(alphab[_Dindex])
    print ''.join(desifrirana_lista)


while True:
    vprasanje1 = raw_input('Ali zelis sifrirati text DA/NE: ').upper()
    # Ce da potem zacni program - funkcijo, ki bo sifriral
    if vprasanje1 == 'DA':
        sifriranje()
    else:
        vprasanje2 = raw_input('Ali zelis desifrirati text DA/NE: ').upper()
        # Ce da potem zazeni program - funkcijo za desifriranje

        if vprasanje2 == 'DA':
            desifriranje()
        elif vprasanje2 == 'NE':
            # Zapri/koncaj program
            break
