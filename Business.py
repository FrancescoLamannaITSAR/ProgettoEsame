import Persistence
import Scraping
import pandas as pd

class Scheda:
    #In scrittura
    def __init__(self, dati, ID=None):
        if ID is None:
            self.ID = Persistence.nuovoID()
            self.nome = dati['Nome']
            self.razza = dati['Razza']
            self.classe = dati['Classe']
            self.livello = 3
            self.caratteristiche = dati['Caratteristiche']
            self.bonus_competenza = 2 
            dadoVita = int(Scraping.findDV(self.classe))
            self.punti_vita = dadoVita + (1 + dadoVita // 2) * (self.livello - 1) + self.bonusCaratteristica('Costituzione') * self.livello
            self.iniziativa = int(self.bonusCaratteristica('Destrezza'))
            self.velocita = 9
            self.competenze = Scraping.findTS(self.classe) + dati['Competenze']
            self.tiri_salvezza = self.costruisciTiriSalvezza()
            self.abilità = self.costruisciAbilità()
            Persistence.creaScheda(self.__dict__)
        else:
            print(f"Lettura: dati = {dati}, ID = {ID}")
            self.ID = ID
            #Dati da persistance che scrivo sul mio oggetto
            lettura = Persistence.leggi_scheda(ID)
            self.nome = lettura['Nome']
            self.razza = lettura['Razza']
            self.classe = lettura['Classe']
            self.livello = lettura['Livello']
            self.caratteristiche = lettura['Caratteristiche']  #PD DataFrame
            self.bonus_competenza = lettura['Bonus Competenza']
            self.punti_vita = lettura['Punti Vita']
            self.iniziativa = lettura['Iniziativa']
            self.velocita = lettura['Velocita']
            self.competenze = lettura['Competenze']            #PD Array
            self.tiri_salvezza = lettura['Tiri Salvezza']      #PD DataFrame
            self.abilità = lettura['Abilita']                  #PD DataFrame
    
    def __str__(self):
        return (f"Nome: {self.nome} \nRazza: {self.razza} \nClasse: {self.classe} \nLivello: {self.livello} \n"
                f"Punti vita: {self.punti_vita} \nBonus competenza: {self.bonus_competenza} \nIniziativa: {self.iniziativa} \nVelocità: {self.velocita} \n"
                f"\nCaratteristiche: {self.caratteristiche} \n"
                f"\nTiri salvezza: {self.tiri_salvezza} \n"
                f"\nAbilità: {self.abilità} \n"
                f"\nCompetenze:{"".join([f"\n   {comp}" for comp in self.competenze])}\n")
    
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
            'Nome': ['Acrobazia', 'Addestrare Animali', 'Arcano', 'Atletica', 'Furtivita', 'Indagare', 
                'Inganno', 'Intimidire', 'Intrattenere', 'Intuizione', 'Medicina', 'Natura', 
                'Percezione', 'Persuasione', 'Rapidita di Mano', 'Religione', 'Sopravvivenza', 'Storia'],
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

def findAbilitaBU(classe): #Usato per isolare lo scraping dall'interfaccia
    return Scraping.findAbilita(classe)

def infoBoxBU():        #Usato per isolare la persistance dall'interfaccia
    return Persistence.infoBox()