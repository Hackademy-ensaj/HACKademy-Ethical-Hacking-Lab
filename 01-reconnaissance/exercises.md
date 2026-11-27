# Exercices — Reconnaissance

## Level 2 — Practice

### Exercice 1 — Consulter des informations DNS
**But :** comprendre comment `dig` interroge le DNS.

**Énoncé :** demande l'information A pour `scanme.nmap.org`, puis demande les types MX et NS du domaine `nmap.org`. Ces consultations DNS ne t'autorisent pas à scanner d'autres hôtes.

**Méthode :**
1. Lance les trois commandes présentées dans la leçon.
2. Repère le nom demandé et le type d'enregistrement dans chaque commande.
3. Compare les lignes retournées. Si tu n'obtiens rien, vérifie le nom et le type.

**Observe et note :** le type demandé, le nombre de lignes retournées et ce que signifie chaque type. Ne recopie pas une sortie comme si elle était permanente : le DNS peut changer.

<details>
<summary>Indice 1</summary>

Dans `dig`, le type (`A`, `MX` ou `NS`) se place juste après le nom demandé.
</details>

<details>
<summary>Indice 2</summary>

`+short` réduit l'affichage. Chaque ligne représente une valeur renvoyée par le DNS ; interprète-la selon le type demandé.
</details>

### Exercice 2 — Lire les en-têtes HTTP
**But :** distinguer les en-têtes du contenu d'une réponse.

**Énoncé :** demande la page d'accueil du serveur local et affiche les en-têtes avec le contenu.

**Méthode :**
1. Vérifie que le serveur du lab tourne.
2. Utilise `curl -i` vers `http://127.0.0.1:8080/`.
3. Repère la ligne de statut, les en-têtes et la séparation avec le contenu.

**Observe et note :** le statut HTTP, les noms d'en-têtes présents et la différence entre en-têtes et contenu. Ne déduis pas plus que ce que la réponse montre.

<details>
<summary>Indice 1</summary>

`-i` demande à `curl` d'afficher les en-têtes de réponse avec le contenu.
</details>

<details>
<summary>Indice 2</summary>

La ligne vide sépare les en-têtes du contenu. La première ligne commence par la version HTTP et un code de statut.
</details>

### Exercice 3 — Examiner `robots.txt` et le HTML
**But :** repérer des informations qui ont été publiées par erreur.

**Énoncé :** lis `robots.txt` et le code HTML de la page d'accueil locale. Cherche les types d'informations qui pourraient aider un développeur, sans supposer qu'une consigne constitue une protection.

**Méthode :**
1. Demande le chemin `/robots.txt` avec `curl -s`.
2. Demande la page d'accueil avec `curl -i`.
3. Distingue les directives du fichier texte du commentaire éventuellement présent dans le HTML.

**Observe et note :** quelles catégories d'information sont visibles ? Pourquoi ne faut-il pas mettre un secret dans un fichier public ? N'inscris pas de flag, de mot de passe ou de solution dans ce fichier.

<details>
<summary>Indice 1</summary>

Le fichier `robots.txt` est un document texte. La page d'accueil est une réponse HTML.
</details>

<details>
<summary>Indice 2</summary>

Dans le HTML, cherche les marqueurs de commentaires. Dans `robots.txt`, rappelle-toi que les consignes pour les robots ne bloquent pas une visite directe.
</details>

## Level 3 — Challenge

**But :** appliquer la reconnaissance pour trouver une information de développement exposée sur la cible du lab, sans recevoir directement le chemin.

**Énoncé :** enchaîne les observations des exercices. Reste sur `127.0.0.1`. Ne devine pas des identifiants et ne teste aucune autre machine.

**Méthode :** pars d'une ressource publique déjà observée, formule une hypothèse, puis vérifie-la avec une requête HTTP simple. Si tu obtiens une erreur, relis le code de statut et vérifie ton chemin.

**Observe et note :** conserve dans tes notes personnelles la ressource consultée, la commande, le statut reçu et ce que tu as appris. Ne mets aucun flag ni réponse dans les fichiers Markdown du dépôt.

<details>
<summary>Indice 1</summary>

Les ressources publiques peuvent contenir des références vers d'autres chemins. Relis les observations précédentes.
</details>

<details>
<summary>Indice 2</summary>

Un commentaire dans le HTML peut donner une piste. Une piste n'est pas la réponse : vérifie-la uniquement sur le serveur local.
</details>
