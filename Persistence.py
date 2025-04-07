import json

def nuovoID():
    with open('Sheets.json') as file:
        data = json.load(file)
        return(len(data))
    return -1

def creaScheda(scheda):
    try:
        with open('Sheets.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        scheda = {
            (k if k == "ID" else k.replace("_", " ").title()): v 
            for k, v in scheda.items()
        }
        
        for chiave in ["Caratteristiche", "Tiri Salvezza", "Abilità"]:  #Converto il DF di pandas in un dizionario
            scheda[chiave] = {row["Nome"]: row["Valore"] for _, row in scheda[chiave].iterrows()}
        scheda["Punti Vita"] = int(scheda["Punti Vita"])
        data.append(scheda)

        with open('Sheets.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        print(f"Errore durante la scrittura del file: {e}"
              f"\nEcco i dati:\n {data}")
        
def leggi_scheda(ID: int):
    with open('Sheets.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    for scheda in data:
        if scheda["ID"] == int(ID):
            return scheda
    print(f"Nessuna scheda trovata con ID {ID}")

def infoBox():
    with open('Sheets.json') as file:
        data = json.load(file)
    str = ''
    for d in data:
        str += (f"ID: {d['ID']}. Personaggio: {d['Nome']} ({d['Razza']} - {d['Classe']}).\n")
    return str