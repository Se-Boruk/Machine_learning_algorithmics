import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools
from scipy.spatial.distance import cosine


#Ladowanie danych
df = pd.read_csv("glosowanie.csv")

#Wyrzucenie niepotrzebnych tematow (np. przerwe)
values_to_drop = [
                    "Wniosek o skrócenie terminów",
                    "Wniosek o przerwę",
                    "Wniosek o przedłużenie posiedzenia",
                    "Wniosek o zmianę porządku dnia",
                    "Wniosek o uzupełnienie porządku dziennego",
                    "Wniosek o przejście do porządku dziennego",
                ]

df = df[~df['temat'].isin(values_to_drop)]


#Przekształć dane do formy, w której każdy klub jest reprezentowany jako wektor.
kluby = np.unique(df['klub'])


nazwy = {"KO": "KO",
         "Kondefedacja": "Konfederacja",
         "Kukiz15": "Kukuz15",
         "Lewica": "Lewica",
         "Nowa_Lewica": "Lewica",
         "PSL": "PSL",
         "PSL-TD": "PSL",
         "PiS": "PiS",
         "Polska2050": "Polska2050",
         "Polska2050-TD": "Polska2050",
         "Razem": "Razem",
         "Republikanie": "Republikanie",
         "niez.": "niez."
        }

#Zmiana nazw klubow na jednolite
for key, value in nazwy.items():
    df.loc[df['klub'] == key, 'klub'] = value
    
#Wyprinowac wszystkie kluby po ujednoliceniu nazw klubow:
kluby = np.unique(df['klub'])
print("Kluby po unifikacji nazwy:")
for k in kluby:
    print(k)

#Wektor przygotowanie
wektor = {}
for klub in kluby:
    wektor[klub] = []

#Unikalne glosowania
glosowania = np.unique(df['id'])

for i in glosowania:
    #Wybierz to glosowanie
    df_glos = df.loc[df['id'] == i]
    for klub in kluby:
        #Wybierz kolumne glos dla danego klubu
        a = df_glos.loc[df_glos['klub'] == klub, 'glos']
        Vote_yes = 1 if (a == 'YES').any() else 0
        wektor[klub].append(Vote_yes)

#Pary partii
pairs = list(itertools.combinations(wektor.keys(), 2))

best_cos_pair = None
best_cos_distance = np.inf

worst_cos_pair = None
worst_cos_distance = 0
print("------------------------------------------------------------")
print("Sprawdzanie najbardziej podobnie glosujacych i najmniej podobnie glosujacych klubow")
for p in pairs:
    p0 = wektor[p[0]]
    p1 = wektor[p[1]]
    
    distance_cos = cosine( p0, p1 )
    
    #Cosine pair (most matching clubs)
    if distance_cos < best_cos_distance:
        best_cos_distance = distance_cos
        best_cos_pair = p
        
    #Cosine pair (least matching clubs)
    if distance_cos > best_cos_distance:
        worst_cos_distance = distance_cos
        worst_cos_pair = p

print("Najpodobniejsze kluby: ", best_cos_pair[0],';', best_cos_pair[1])
print("Najrozniejsze kluby: ", worst_cos_pair[0],';', worst_cos_pair[1])
print("------------------------------------------------------------")
print("Sprawdzanie ktory klub jest najbardziej odmienny od pozostalych")

Roznice = {}
for k in wektor.keys():
    k_list = list(wektor.keys())
    k_list.remove(k)
    
    distance_sum = 0

    for other_k in k_list:
        distance_cos = cosine(wektor[k], wektor[other_k])
        distance_sum += distance_cos
        
    Roznice[k] = distance_sum
print("Dystans do innych klubów")    
for key, value in Roznice.items():
    print("Klub",key,":",round(value,2))
    
#Klub z maks odlegloscia
max_key = max(Roznice, key=Roznice.get)
print("\nNajodmienniej glosujacym klubem jest: ",max_key)














