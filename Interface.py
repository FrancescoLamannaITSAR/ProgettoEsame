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
    dati['Nome'] = input("Come si chiama il tuo eroe? ")
    dati['Razza'] = input_elenco('razza', razze)
    dati['Classe'] = input_elenco('classe', classi)
    dati['Caratteristiche'] = input_caratteristiche()
    dati['Competenze'] = input_competenze(dati['Classe'])
    scheda = Business.Scheda(dati)
    print("Scheda salvata con i seguenti dati:\n", scheda)

def leggi_scheda():
    print(Business.infoBoxBU())
    ID = input("Inserisci l'ID della scheda da leggere: ")
    scheda = Business.Scheda([], ID=ID)
    print("", scheda)
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

def input_competenze(classe):
    if classe == "Bardo":   #Non ho bisogno di fare scraping, perchè il bardo può scegliere tra tutte
        ab = ['Acrobazia', 'Addestrare Animali', 'Arcano', 'Atletica', 'Furtivita', 'Indagare', 
                'Inganno', 'Intimidire', 'Intrattenere', 'Intuizione', 'Medicina', 'Natura', 
                'Percezione', 'Persuasione', 'Rapidita di Mano', 'Religione', 'Sopravvivenza', 'Storia']
        return scegli_competenze(ab, 3)
    else:
        if classe == "Ladro":
            n = 4
        elif classe == "Ranger":
            n = 3
        else:
            n = 2
        return scegli_competenze(Business.findAbilitaBU(classe), n)

def scegli_competenze(abilità_disponibili, numero_da_scegliere):
    competenze_selezionate = []
    print(f"\nScegli {numero_da_scegliere} competenze tra le seguenti:")
    # Crea una lista numerata delle abilità disponibili
    while len(competenze_selezionate) < numero_da_scegliere:
        # Mostra le abilità disponibili, aggiornando l'elenco ogni volta
        for i, abilita in enumerate(abilità_disponibili, 1):
            print(f"{i}. {abilita}")

        try:
            # Chiedi all'utente di scegliere un numero
            scelta = int(input(f"Seleziona la competenza {len(competenze_selezionate) + 1}/{numero_da_scegliere}: "))

            # Verifica che la scelta sia valida
            if scelta < 1 or scelta > len(abilità_disponibili):
                print("Scelta non valida, riprova.")
            else:
                competenza_scelta = abilità_disponibili[scelta - 1]

                # Aggiungi la competenza scelta alla lista e rimuovila dall'elenco disponibile
                if competenza_scelta not in competenze_selezionate:
                    competenze_selezionate.append(competenza_scelta)
                    abilità_disponibili.remove(competenza_scelta)  # Rimuove l'abilità scelta
                else:
                    print("Questa competenza è già stata selezionata, riprova.")
        except ValueError:
            print("Per favore, inserisci un numero valido.")

    print(f"Competenze selezionate: {', '.join(competenze_selezionate)}")
    return competenze_selezionate

print("Avventuriero, benvenuto nel programma di creazione schede per D&D!")
menu()