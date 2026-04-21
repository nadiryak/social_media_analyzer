# 🌐 Social Network Analyzer

> **NOTE:** This project is still in progress. The `influential_node` function is not implemented yet — I'm working on it.

This is a simple social network analyzer written in Python. I built it to practice graph theory concepts from my algorithms course — things like adjacency lists, DFS, and cycle detection.

The original exercise was simpler — just basic and it was about lists.
But I was curious, so I asked questions and went deeper and i found myself learning graphs stuff without even knowing😁:
cycle detection, centrality, influential nodes.
Everything beyond the basics came from my own exploration.

---

## 📌 How I model the network

I represent the network as an **adjacency list**. Each index is a person, and the list at that index contains the people they follow.

```python
RESEAU = [
    [1, 2],      # person 0 follows 1 and 2
    [2],         # person 1 follows 2
    [0, 1, 3],   # person 2 follows 0, 1 and 3
    [],          # person 3 follows nobody
    [0, 1, 3]    # person 4 follows 0, 1 and 3
]
```

---

## ⚙️ What the project does

### Count edges
`nbr_de_edges(reseau)` counts the total number of connections in the network. I just sum the length of each list.

```python
nbr_de_edges(RESEAU)  # → 9
```

---

### Count followers
`nbr_de_followers(person, reseau)` counts how many people follow a given person. I go through every list and check if that person appears in it.

```python
nbr_de_followers(2, RESEAU)  # → 3 (persons 0, 1 and 4 follow person 2)
nbr_de_followers(3, RESEAU)  # → 1 (only person 2 follows person 3)
```

---

### Most followed person
`la_personne_la_plus_suivie(reseau)` finds who has the most followers. I build a list of follower counts for everyone, then find the maximum.

```python
la_personne_la_plus_suivie(RESEAU)
# → La personne la plus suivie est 2 avec 3 abonnés.
```

---

### Person who follows the most people
`la_personne_qui_suit_plus_de_personne(reseau)` finds who has the most followings. I compare the length of each person's list.

```python
la_personne_qui_suit_plus_de_personne(RESEAU)
# → La personne qui suit le plus de gens est 2 avec 3 followings
```

---

### DFS — exploring the network
`dfs(reseau, start)` explores the network starting from a given person. It visits every person reachable by following connections, without visiting the same person twice.

I use recursion — the function calls itself on each unvisited neighbor.

```python
dfs(RESEAU, 0)
# On visite la personne 0
# On visite la personne 1
# On visite la personne 2
# On visite la personne 3
# → {0, 1, 2, 3}
```

Person 4 is not reachable from 0, so it's not in the result.

---

### Cycle detection
`cycle_detecte(reseau, start)` checks if there is a cycle reachable from a given person.

I use DFS with two sets:
- `visited` — everyone I've already seen
- `en_cours` — everyone on the **current path**

If I reach a person who is already on the current path, there's a cycle.

```python
cycle_detecte(RESEAU, 0)  # → True  (0 follows 2, and 2 follows 0)
cycle_detecte(RESEAU, 3)  # → False (person 3 follows nobody)
```

---

### 🚧 Influential node — to be implemented

I will add a function `noeud_influent(reseau)` that finds the most influential person in the network.

My plan: score each person using **followers + followings**. The person with the highest score is the most influential — they are both well followed and well connected.

I already have `nbr_de_followers` and `len(reseau[i])`, so I just need to combine them.

---

## 🚀 How to run

No external libraries needed. Just Python 3.

```bash
python social_media_analyzer.py
```
