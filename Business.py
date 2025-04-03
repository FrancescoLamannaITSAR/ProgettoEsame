import Persistence
import pandas as pd

class Scheda:
    #In lettura
    def __init__(self, dati, bob):
        self.bob = bob      #placeholder per il bob
        self.ID = dati['ID']
        self.nome = dati['Nome']
        self.razza = dati['Razza']
        self.classe = dati['Classe']
        self.livello = dati['Livello']
        self.caratteristiche = dati['Caratteristiche']  #PD DataFrame
        self.bonus_competenza = dati['Bonus Competenza']
        self.punti_vita = dati['Punti Vita']
        self.iniziativa = dati['Iniziativa']
        self.velocita = dati['Velocità']
        self.competenze = dati['Competenze']            #PD Array
        self.tiri_salvezza = dati['Tiri Salvezza']      #PD DataFrame
        self.abilità = dati['Abilità']                  #PD DataFrame

    #In scrittura
    def __init__(self, dati):
        #DEFINIT
        self.ID = Persistence.nuovoID()
        self.nome = dati['Nome']
        self.razza = dati['Razza']
        self.classe = dati['Classe']
        self.livello = 3
        self.caratteristiche = dati['Caratteristiche']
        self.bonus_competenza = 2 
        self.punti_vita = ("dVita + (1+dVita/2) * (LIV-1)") #TODO: ruba da classe
        self.iniziativa = int(self.bonusCaratteristica('Destrezza'))
        self.velocita = 9 #TODO: Ruba da razza
        self.competenze = dati['Competenze']    #TODO: rivedere
        self.tiri_salvezza = self.costruisciTiriSalvezza()  #TODO: forse finiti
        self.abilità = self.costruisciAbilità() #TODO: forse finiti
        Persistence.creaScheda(self.__dict__)
    
    def __str__(self):
        return (f"Nome: {self.nome} \nRazza: {self.razza} \nClasse: {self.classe} \nLivello: {self.livello} \n"
                f"Punti vita: {self.punti_vita} \nBonus competenza: {self.bonus_competenza} \nIniziativa: {self.iniziativa} \nVelocità: {self.velocita} \n"
                f"\nCaratteristiche: {self.caratteristiche} \n"
                f"\nTiri salvezza: {self.tiri_salvezza} \n"
                f"\nAbilità: {self.abilità} \n"
                f"\nCompetenze:{"".join([f"\n   {k}: {v}" for k, v in self.competenze.items()])}\n")
    
    def bonusCaratteristica(self, car):
        valore = self.caratteristiche.loc[self.caratteristiche["Nome"] == car, "Valore"].values[0]
        return (valore - 10) // 2

    def costruisciTiriSalvezza(self):
        TS = pd.DataFrame({  
            'Nome': ['Forza', 'Destrezza', 'Costituzione', 'Intelligenza', 'Saggezza', 'Carisma'],
            'Valore': [self.bonusCaratteristica("Forza"),
                       self.bonusCaratteristica("Destrezza"),
                       self.bonusCaratteristica("Costituzione"),
                       self.bonusCaratteristica("Intelligenza"),
                       self.bonusCaratteristica("Saggezza"),
                       self.bonusCaratteristica("Carisma")]
        })
        TS = applicaBonusCompetenza(TS, self.competenze, self.bonus_competenza)
        return TS  

    def costruisciAbilità(self):
        A = pd.DataFrame({
            'Nome': ['Acrobazia', 'Addestrare Animali', 'Arcano', 'Atletica', 'Furtività', 'Indagare', 
                'Inganno', 'Intimidire', 'Intrattenere', 'Intuizione', 'Medicina', 'Natura', 
                'Percezione', 'Persuasione', 'Rapidità di Mano', 'Religione', 'Sopravvivenza', 'Storia'],
            'Valore': [self.bonusCaratteristica("Destrezza"),
                self.bonusCaratteristica("Saggezza"),
                self.bonusCaratteristica("Intelligenza"),
                self.bonusCaratteristica("Forza"),
                self.bonusCaratteristica("Destrezza"),
                self.bonusCaratteristica("Intelligenza"),
                self.bonusCaratteristica("Carisma"),
                self.bonusCaratteristica("Carisma"),
                self.bonusCaratteristica("Carisma"),
                self.bonusCaratteristica("Saggezza"),
                self.bonusCaratteristica("Saggezza"),
                self.bonusCaratteristica("Intelligenza"),
                self.bonusCaratteristica("Saggezza"),
                self.bonusCaratteristica("Carisma"),
                self.bonusCaratteristica("Destrezza"),
                self.bonusCaratteristica("Intelligenza"),
                self.bonusCaratteristica("Saggezza"),
                self.bonusCaratteristica("Intelligenza")]
        })
        A = applicaBonusCompetenza(A, self.competenze, self.bonus_competenza)
        return A

def applicaBonusCompetenza(df, competenze, bonus_competenza):
    df['Competenza'] = df['Nome'].isin(competenze)     # Aggiungiamo la serie di competenze a df, per verificare dove c'è competenza
    df['Valore'] += df['Competenza'] * bonus_competenza # Applichiamo il bonus solo a chi ha la competenza
    df.drop(columns='Competenza', inplace=True)
    return df