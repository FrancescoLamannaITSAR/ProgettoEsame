import json

def nuovoID():
    with open('Sheets.json') as file:
        data = json.load(file)
        return(len(data) + 1)
    return -1

def creaScheda(scheda):
    with open('Sheets.json') as file:
        data = json.load(file)
    data.append(scheda)
    with open('Sheets.json', 'w') as file:
        json.dump(data, file, indent=4)

def infoBoxPe():
    with open('Sheets.json') as file:
        str = ''
        data = json.load(file)
        for d in data:
            str += (f"ID: {d['ID']}, Intestatario: {d['intestatario']}, IBAN: {d['IBAN']}\n")
    return str