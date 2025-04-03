import json

def nuovoID():
    with open('Sheets.json') as file:
        data = json.load(file)
        return(len(data) + 1)
    return -1

def creaScheda(scheda):
    try:
        with open('Sheets.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        scheda = {k.replace("_", " ").title(): v for k, v in scheda.items()}
        
        for chiave in ["Caratteristiche", "Tiri Salvezza", "Abilità"]:  #Converto il DF di pandas in un dizionario
            scheda[chiave] = {row["Nome"]: row["Valore"] for _, row in scheda[chiave].iterrows()}
        scheda["Competenze"] = scheda["Competenze"].tolist()
        
        data.append(scheda)

        with open('Sheets.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            
    except Exception as e:
        print(f"Errore durante la scrittura del file: {e}"
              f"\nEcco i dati:\n {data}")

def infoBoxPe():
    with open('Sheets.json') as file:
        str = ''
        data = json.load(file)
        for d in data:
            str += (f"ID: {d['ID']}, Intestatario: {d['intestatario']}, IBAN: {d['IBAN']}\n")
    return str