RESEAU = [
    [1, 2],      # 0 follow 1 et 2
    [2],         # 1 follow 2
    [0, 1, 3],   # 2 follow 0,1,3
    [],          # 3 follow personne
    [0, 1, 3]    # 4 follow 0,1,3
]
print("!!!!!!!!!!!!!!!! ON COMMENCE PAR L'ANALYSE D'UN RESEAU SOCIAL !!!!!!!!!!!!!!!!!!!!!!!!!")
g=input("POUR COMMENCER APPUIE SUR N'IMPORTE QUEL TOUCHE ")

def nbr_de_edges(reseau):
    cpt=0
    for res in reseau:
        cpt+=len(res)
    return cpt



def nbr_de_followers(pers,reseau):
    if pers>=len(reseau):
        return "ERROR: votre personne n'existe pas dans notre liste (INDEX OUT OF RANGE)"
    else:
        nb=0
        for p in reseau:
            if pers in p :
                nb+=1
        return nb



def la_personne_la_plus_suivie(reseau):
    liste_nbr_follower= []
    i=0
    for pers in reseau :
        liste_nbr_follower.append(nbr_de_followers(i,reseau))
        i+=1
    maximum=max(liste_nbr_follower)    
    personne=liste_nbr_follower.index(max(liste_nbr_follower))
    print(f"La personne la plus suivie par les gense est {personne} avec {maximum} abonnées. ")
    return(personne, maximum)


def la_personne_qui_suit_plus_de_personne(reseau):
    if not reseau:
        return "Votre liste de reseau est vide "
    else:
        maximum =len(reseau[0])
        personne=0
        i=0
        for pers in reseau:
            
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
    



def cycle_detecte(reseau):
    for i in range(reseau):
        for pers in reseau[i]:
            if i in pers:
                detect=True
                break
            else:
                None

    
def dfs(reseau, start, visited=None):
    if visited is None:
        visited = set()  # ensemble des personnes déjà visitées
    
    visited.add(start)  #  la personne est visitée
    print(f"On visite la personne {start}")

    for voisin in reseau[start]:  # explore toutes les personnes suivies
        if voisin not in visited:
            dfs(reseau, voisin, visited) 
        else: 
            return True
        

    return visited
