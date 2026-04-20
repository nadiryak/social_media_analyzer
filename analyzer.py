RESEAU = [
    [1, 2],      # 0 follow 1 et 2
    [2],         # 1 follow 2
    [0, 1, 3],   # 2 follow 0,1,3
    [],          # 3 follow personne
    [0, 1, 3]    # 4 follow 0,1,3
]
print("!!!!!!!!!!!!!!!! ON COMMENCE PAR L'ANALYSE D'UN RESEAU SOCIAL !!!!!!!!!!!!!!!!!!!!!!!!!")
g=input("POUR COMMENCER APPUIE SUR N'IMPORTE QUEL TOUCHE ")

def nbr_de_edges(reseau):  # on compte tous les arcs du graphe en additionnant la taille de chaque liste
    cpt=0
    for res in reseau:
        cpt+=len(res)
    return cpt



def nbr_de_followers(pers,reseau):
    if pers>=len(reseau):
         # on vérifie que la personne existe dans le réseau
        return "ERROR: votre personne n'existe pas dans notre liste (INDEX OUT OF RANGE)"
    else:
        nb=0
        for p in reseau:
             # si "pers" apparaît dans la liste de suivis de p
             # ça veut dire que p suit "pers" -> p est un follower de "pers"
            if pers in p :
                nb+=1
        return nb



def la_personne_la_plus_suivie(reseau):        
    # on construit la liste du nombre de followers pour chaque personne
    liste_nbr_follower= []
    i=0
    for pers in reseau :
        liste_nbr_follower.append(nbr_de_followers(i,reseau))
        i+=1
    # puis on cherche l'index du maximum = la personne la plus suivie
    maximum=max(liste_nbr_follower)    
    personne=liste_nbr_follower.index(max(liste_nbr_follower))
    print(f"La personne la plus suivie par les gense est {personne} avec {maximum} abonnées. ")
    return(personne, maximum)


def la_personne_qui_suit_plus_de_personne(reseau):
    if not reseau:
        return "Votre liste de reseau est vide "
    else:
        maximum =len(reseau[0]) # on initialise avec la première personne comme référence
        personne=0
        i=0
        for pers in reseau:    # on parcourt pour trouver celle qui a la liste la plus longue
            
            if len(pers)>maximum:
                maximum=len(pers)
                personne=i
                i+=1
            else:
                i+=1
                continue 
        s=f"la personne qui suit plus des autres gens est {personne} avec {maximum} followings "
        # JUSTE POUR SAVOIR COMMENT MARCHE ENUMERATE ICI    
#         maximum = -1
#         personne = -1
#   for i, pers in enumerate(reseau):
#     if len(pers) > maximum:
#         maximum = len(pers)
#         personne = i
        return s


#CETTE FONCTION A ETE APPRISE POUR DES RAISONS D'APPRENTISSAGE ET PAR CURIOSITE POUR POOUVOIR DETECTER LES CYCLE DANS LE PROGRAME D'APRES    
def dfs(reseau, start, visited=None):
    if visited is None:
        visited = set()  # ensemble des personnes déjà visitées
    
    visited.add(start)  #  la personne est visitée
    print(f"On visite la personne {start}")

    for voisin in reseau[start]:  # explore toutes les personnes suivies
        if voisin not in visited:
            dfs(reseau, voisin, visited)  
    return visited


def cycle_detecte(reseau, start, visited=None, en_cours=None):
     if visited is None:          #initaliser visited et en_cours si elles sont vide 
        visited = set()
    if en_cours is None:
        en_cours = set()
    
    visited.add(start)   # on marque le nœud comme visité et comme "en cours de visite sur ce chemin"
    en_cours.add(start)    
   for suivie in reseau[start]:
       
       if suivie in en_cours:  # si on retombe sur un nœud qu'on est en train de visiter 
           return True  # Cycle détecté
      # si la personne suivie n'a pas encore été visité, on plonge dedans
      # si l'appel récursif détecte un cycle, on return True 
       if suivie not in visited:
           if cycle_detecte(reseau,suivie,visited,en_cours):
               return True
               
   # on repart en arrière,ce nœud n'est plus sur le chemin actuel           
   en_cours.remove(start)
   return False

    

