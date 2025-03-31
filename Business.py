class Scheda:
    #In lettura
    def __init__(self, dati):
        self.nome = dati['Nome']
        self.razza = dati['Razza']
        self.classe = dati['Classe']
        self.livello = dati['Livello']
        self.punti_vita = dati['Punti vita']
        self.iniziativa = dati['Iniziativa']
        self.velocita = dati['Velocità']
        self.caratteristiche = dati['Caratteristiche']
        self.tiri_salvezza = dati['Tiri salvezza']
        self.abilita = dati['Abilità']
        self.competenze = dati['Competenze']

    #In scrittura
    def __init__(self, dati):
            #Anagrafica input
        self.nome = dati['Nome']
        self.razza = dati['Razza']
        self.classe = dati['Classe']
        self.livello = dati['Livello']
            #Valori Input
        self.caratteristiche = dati['Caratteristiche']
        self.competenze = dati['Competenze']
            #Anagrafica calcolati
        self.punti_vita = ("dVita + (1+dVita/2) * (LIV-1)") #TODO: ruba da classe
        self.iniziativa = self.bonusCaratteristica('Destrezza')
        self.velocita = dati['Velocità'] #TODO: Ruba da razza
            #Valori calcolati
        self.costruisciTiriSalvezza(dati)
        self.costruisciAbilità(dati)
    
    def bonusCaratteristica(self, car):
        return ((self.caratteristiche[car]-10) / 2)

    def costruisciTiriSalvezza(self, dati):
        TS = {  #Imposto i valori base
            "Forza": self.bonusCaratteristica("Forza"),
            "Destrezza": self.bonusCaratteristica("Destrezza"),
            "Costituzione": self.bonusCaratteristica("Costituzione"),
            "Intelligenza": self.bonusCaratteristica("Intelligenza"),
            "Saggezza": self.bonusCaratteristica("Saggezza"),
            "Carisma": self.bonusCaratteristica("Carisma")
        }
        for k, v  in TS.items():    #Poi applico il bonus competenza dove serve
            TS[k] = applicaBonusCompetenza(v, k, dati['Competenze']['Tiri Salvezza'], dati['Competenze']['Bonus Competenza'])
        self.tiri_salvezza = TS
        pass

    def costruisciAbilità(self, dati):
        A = {
            "Acrobazia": self.bonusCaratteristica("Destrezza"),
            "Addestrare Animali": self.bonusCaratteristica("Saggezza"),
            "Arcano": self.bonusCaratteristica("Intelligenza"),
            "Atletica": self.bonusCaratteristica("Forza"),
            "Furtività": self.bonusCaratteristica("Destrezza"),
            "Indagare": self.bonusCaratteristica("Intelligenza"),
            "Inganno": self.bonusCaratteristica("Carisma"),
            "Intimidire": self.bonusCaratteristica("Carisma"),
            "Intrattenere": self.bonusCaratteristica("Carisma"),
            "Intuizione": self.bonusCaratteristica("Saggezza"),
            "Medicina": self.bonusCaratteristica("Saggezza"),
            "Natura": self.bonusCaratteristica("Intelligenza"),
            "Percezione": self.bonusCaratteristica("Saggezza"),
            "Persuasione": self.bonusCaratteristica("Carisma"),
            "Rapidità di Mano": self.bonusCaratteristica("Destrezza"),
            "Religione": self.bonusCaratteristica("Intelligenza"),
            "Sopravvivenza": self.bonusCaratteristica("Saggezza"),
            "Storia": self.bonusCaratteristica("Intelligenza")
        }
        for k, v  in A.items():    #Poi applico il bonus competenza dove serve
            A[k] = applicaBonusCompetenza(v, k, dati['Competenze']['Abilità'], dati['Competenze']['Bonus Competenza'])
        self.abilita = A

#Se NOME compare nella lista COMPETENZE, applico il BONUS sommandolo al VALORE
def applicaBonusCompetenza(valore, nome, competenze, bonus):
    for c in competenze:
        if(nome == c):
            return (valore + bonus)
    return valore
    pass