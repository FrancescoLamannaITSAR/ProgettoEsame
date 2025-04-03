import random, time, pandas as pd
import Business

razze = [
    (1, "Aasimar"), (2, "Draconide"), (3, "Elfo"), (4, "Gnomo"), (5, "Goliath"), 
    (6, "Halfling"), (7, "Nano"), (8, "Orco"), (9, "Tiefling"), (10, "Umano")
]
classi = [
    (1, "Barbaro"), (2, "Bardo"), (3, "Chierico"), (4, "Druido"), (5, "Guerriero"),
    (6, "Ladro"), (7, "Mago"), (8, "Monaco"), (9, "Paladino"), (10, "Ranger"), (11, "Stregone"), (12, "Warlock")
]

def menu():
    while True:
        print("Menu:")
        print("1. Scrivi una scheda")
        print("2. Leggi una scheda")
        print("3. Modifica una scheda")
        print("q. Esci")
        scelta = input("Seleziona un'opzione (1/2/3/q): ")

        if scelta == "1":
            scrivi_scheda()
        elif scelta == "2":
            leggi_scheda()
        elif scelta == "3":
            modifica_scheda()
        elif scelta == "q":
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida. Riprova.")

def scrivi_scheda():
    dati = {}
    dati['Nome'] = input("Come si chiama il tuo eroe? ")    #TODO: controlla se esiste già
    dati['Razza'] = input_elenco('razza', razze)
    dati['Classe'] = input_elenco('classe', classi)
    dati['Caratteristiche'] = input_caratteristiche()
    dati['Competenze'] = input_competenze() #TODO: Scratchare abilità e TS da classe
    scheda = Business.Scheda(dati)
    print("Scheda salvata con i seguenti dati:\n", scheda)

def leggi_scheda():
    print("Funzione per leggere una scheda.")
    # Implementa qui la logica per leggere una scheda

def modifica_scheda():
    print("Funzione per modificare una scheda.")
    # Implementa qui la logica per modificare una scheda

def input_elenco(tipo, lista):
     print(f"Scegliamo la {tipo}:")
     while True:
        try:
            print(lista)
            scelta = int(input(f"Inserisci il numero corrispondente alla {tipo}: "))
            if 1 <= scelta <= len(lista):
                print(f"Hai scelto: {lista[scelta - 1][1]}")    #Prendo il secondo elemento della tupla, dentro la lista
                return(lista[scelta - 1][1])
            else:
                print("Numero non valido. Riprova.")
        except ValueError:
            print("Input non valido. Inserisci un numero.")

def input_caratteristiche():
    scores = []
    caratteristiche = pd.DataFrame({
        'Nome': ['Forza', 'Destrezza', 'Costituzione', 'Intelligenza', 'Saggezza', 'Carisma'],
        'Valore': [-1, -1, -1, -1, -1, -1]})
    input('Tiriamo i punteggi per le caratteristiche, 6 serie di 4 dadi a 6 facce, cui tolto il valore più basso, vengono sommati. >>>')

    for i in range (6):
        list = []
        tot = 0
        for j in range (4):
            list.append(random.randint(1,6))
        list.sort(reverse = True)
        list[len(list)-1] = [list[len(list)-1]]
        print(list, ' -> ', sum(list[:-1]))
        scores.append(sum(list[:-1]))
        time.sleep(0.5)

    scores.sort(reverse = True)
    print('Ecco i tuoi punteggi: ', scores)
    input('Ora associamo i punteggi alle caratteristiche. >>>')

    for score in scores:
        while True:
            print(f"\nPunteggio da assegnare: {score}")
            print("Caratteristiche disponibili:")
            #Qui
            for i, row in caratteristiche.iterrows():
                if (row["Valore"] == -1):
                    print(f"- {i}: {row['Nome']}")

            scelta = input("A quale statistica vuoi assegnare questo punteggio? (Inserisci l'indice) ")
            
            try:
                indice = int(scelta)  # Prova a convertire l'input in intero
                if indice in caratteristiche.index and caratteristiche.at[indice, "Valore"] == -1:
                    caratteristiche.at[indice, "Valore"] = score  # Assegna il punteggio
                    break  # Esce dal ciclo
                else:
                    print("Indice non valido o statistica già assegnata, riprova.")
            except ValueError:
                print("Inserisci un numero valido.")  # Messaggio d'errore se la conversione fallisce

    print("Caratteristiche finali assegnate:", caratteristiche)
    return caratteristiche

def input_competenze(): #TODO: fare
    comp = pd.Series(["Destrezza", "Intelligenza", "Acrobazia", "Furtività", "Percezione", "Storia"])
    return comp

print("Avventuriero, benvenuto nel programma di creazione schede per D&D!")
menu()