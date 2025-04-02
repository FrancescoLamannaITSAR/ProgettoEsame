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
statistiche = {'F': 'Forza', 'D': 'Destrezza', 'O': 'Costituzione', 'I': 'Intelligenza', 'S': 'Saggezza', 'A': 'Carisma'}

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
    dati['Nome'] = input("Come si chiama il tuo eroe? ")
    dati['Razza'] = input_elenco('razza', razze)
    dati['Classe'] = input_elenco('classe', classi)
    dati['Caratteristiche'] = input_caratteristiche()
    dati['Competenze'] = input("Inserisci le competenze: ") #TODO: Scratchare abilità e TS da classe
    print("Scheda salvata con i seguenti dati:", dati)
    scheda = Business.Scheda(dati)

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
                return(lista[scelta - 1])
            else:
                print("Numero non valido. Riprova.")
        except ValueError:
            print("Input non valido. Inserisci un numero.")

def input_caratteristiche():
    scores = []
    stats = {'Forza' : -1, 'Destrezza' : -1, 'Costituzione' : -1, 'Intelligenza' : -1, 'Saggezza' : -1, 'Carisma' : -1}
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
            print(f"Punteggio da assegnare: {score}")
            print("Statistiche disponibili:")
            for key, stat in statistiche.items():
                if stats[stat] == -1:
                    print(f"- {key}: {stat}")
            scelta = input("A quale statistica vuoi assegnare questo punteggio? (Inserisci la lettera corrispondente) ").upper()
            if scelta in statistiche and stats[statistiche[scelta]] == -1:
                stats[statistiche[scelta]] = score
                break
            else:
                print("Scelta non valida, riprova.")

    print("Caratteristiche finali assegnate:", stats)
    return stats

menu()

