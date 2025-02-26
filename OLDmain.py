import math
import random
import time

originalPDF = open('ProgettoEsame\\DnD_5E_CharacterSheet_FormFillable.pdf', 'r')
sheetTXT = open('ProgettoEsame\\test.txt', 'w')
scores = []
stats = {'Forza' : -1, 'Destrezza' : -1, 'Costituzione' : -1, 'Intelligenza' : -1, 'Saggezza' : -1, 'Carisma' : -1}

print('Benvenuti nella creazione guidata della scheda del personaggio di DnD.')
print('Iniziamo con i punteggi per le caratteristiche, 6 serie di 4 dadi a 6 facce, cui tolto il valore più basso, vengono sommati.')
input()

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
input()

print(f'Ora assegnamo i punti alle caratteristiche: {', '.join([s for s in stats])}.')
stats