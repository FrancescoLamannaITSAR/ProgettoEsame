import requests
from bs4 import BeautifulSoup

ts_ITA = {
    "Strength": "Forza",
    "Dexterity": "Destrezza",
    "Constitution": "Costituzione",
    "Intelligence": "Intelligenza",
    "Wisdom": "Saggezza",
    "Charisma": "Carisma"
}

abilitaIT = {
    "Acrobatics": "Acrobazia",
    "Animal Handling": "Addestrare Animali",
    "Arcana": "Arcano",
    "Athletics": "Atletica",
    "Stealth": "Furtivita",
    "Investigation": "Indagare",
    "Deception": "Inganno",
    "Intimidation": "Intimidire",
    "Performance": "Intrattenere",
    "Insight": "Intuizione",
    "Medicine": "Medicina",
    "Nature": "Natura",
    "Perception": "Percezione",
    "Persuasion": "Persuasione",
    "Sleight of Hand": "Rapidita di Mano",
    "Religion": "Religione",
    "Survival": "Sopravvivenza",
    "History": "Storia"
}

def getSoup(classe):
    with open(rf".\WebPages\{classe} - 5etools.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    return soup

def findDV(classe):
    soup = getSoup(classe)  # Ottieni il soup per la classe
    if soup:
        hit_point_die_line = soup.find(string="Hit Point Die:")  # Cerca la stringa "Hit Point Die:"
        # Se la riga esiste, cerca il testo successivo
        if hit_point_die_line:
            parent = hit_point_die_line.find_parent()  # Trova il parent dell'elemento
            next_sibling = parent.find_next_sibling()  # Cerca il prossimo sibling     
            if next_sibling:
                # Ora estraiamo il dato che contiene "D12" e lo trasformiamo in "12"
                next_text = next_sibling.get_text(strip=True)
                dadoVita = next_text.replace('D', '')  # Rimuove la "D" e lascia solo "12"
                return dadoVita
    return "Punti Ferita non trovati"


def findTS(classe):
    soup = getSoup(classe)  # Ottieni il soup per la classe
    if soup:
        saving_throw_line = soup.find(string="Saving Throw Proficiencies:")  # Cerca la stringa "Saving Throw Proficiencies:"
        if saving_throw_line:
            parent = saving_throw_line.find_parent()  # Trova il parent dell'elemento
            next_sibling = parent.find_next_sibling()  # Cerca il prossimo sibling
            if next_sibling:
                next_text = next_sibling.get_text(strip=True) # Estrai il testo
                ts_lista = []
                for en, it in ts_ITA.items():
                    if en in next_text:
                        ts_lista.append(it)
                return ts_lista
    return ["Tiri Salvezza non trovati"]

def findAbilita(classe):
    soup = getSoup(classe)  # Ottieni il soup per la classe
    if soup:
        skill_proficiencies_line = soup.find(string="Skill Proficiencies:")  # Cerca la stringa "Skill Proficiencies:"
        
        # Se la riga esiste, cerca le righe successive che contengono le abilità
        if skill_proficiencies_line:
            parent = skill_proficiencies_line.find_parent()  # Trova il parent dell'elemento
            next_sibling = parent.find_next_sibling()  # Cerca il prossimo sibling
            if next_sibling:
                # Ora estraiamo il testo delle abilità
                next_text = next_sibling.get_text(strip=True)
                
                # Cerchiamo la stringa "Choose" e rimuoviamo il numero e il ":"
                if "Choose" in next_text:
                    # Rimuoviamo la parte iniziale "Choose X:" dove X è il numero
                    abilita_text = next_text.split(":")[1].strip()
                    
                    # Ora prendiamo tutte le abilità separandole con la virgola
                    abilities = [abilita.strip() for abilita in abilita_text.split(",")]

                    # Rimuovi il prefisso "or" se è presente all'inizio dell'ultima abilità
                    if abilities[-1].startswith("or"):
                        abilities[-1] = abilities[-1][2:].strip()[:-1]  # Rimuove "or" e l'ultimo carattere (punto)

                    # Traduciamo ogni abilità in italiano, se presente nel dizionario
                    abilities_it = [abilitaIT.get(abilita, abilita) for abilita in abilities]

                    return abilities_it
    return "Abilità non trovate"