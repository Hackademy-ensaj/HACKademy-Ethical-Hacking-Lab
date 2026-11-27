# Exercices — Scan et énumération

## Level 2 — Practice

### Exercice 1 — Reconnaître des états de ports
**But :** lire un résultat de scan sans le confondre avec une preuve de vulnérabilité.

**Énoncé :** lance un scan TCP limité sur `127.0.0.1`, avec une plage choisie parmi celles expliquées dans la leçon. Si tu es sous WSL 1, garde à l'esprit que des ports Windows peuvent apparaître.

**Méthode :**
1. Lance la cible locale dans un autre terminal.
2. Utilise `nmap -sT -Pn` et une plage limitée.
3. Repère les colonnes `PORT`, `STATE` et `SERVICE`.
4. Répète avec `-sV` pour comparer l'identification du service.

**Observe et note :** la commande exacte, les états indiqués et la différence entre l'estimation de service et la version détectée. Ne conclus pas qu'un port est vulnérable uniquement parce qu'il est ouvert.

<details>
<summary>Indice 1</summary>

`-sT` sélectionne le type de scan TCP et `-Pn` évite l'étape préalable de détection par ping.
</details>

<details>
<summary>Indice 2</summary>

Compare la colonne `SERVICE` avant et après `-sV`. Sous WSL 1, vérifie si un résultat peut venir de Windows plutôt que du lab.
</details>

### Exercice 2 — Comparer la portée d'un scan
**But :** comprendre qu'une option change le nombre de ports testés.

**Énoncé :** sur `127.0.0.1`, compare un scan rapide et un scan portant sur tous les ports TCP. Ne lance pas ces commandes sur une autre cible.

**Méthode :**
1. Lance `nmap -sT -Pn -F 127.0.0.1`.
2. Lance `nmap -sT -Pn -p- 127.0.0.1`.
3. Compare le temps et le périmètre des résultats.

**Observe et note :** quelle commande examine moins de ports ? Pourquoi un scan plus large peut-il prendre plus de temps ? Note aussi si les résultats sont cohérents avec la cible que tu as lancée.

<details>
<summary>Indice 1</summary>

`-F` demande un scan rapide d'un ensemble réduit de ports ; `-p-` étend le scan à tous les ports TCP.
</details>

<details>
<summary>Indice 2</summary>

Un scan plus large ne signifie pas automatiquement une meilleure explication. Relie chaque résultat à l'option utilisée.
</details>

### Exercice 3 — Observer une bannière
**But :** examiner les informations qu'un service envoie à la connexion.

**Énoncé :** utilise le client Python de la leçon. Indique au programme un port trouvé sur la cible locale et observe la réponse, s'il y en a une. Dans tes explications, remplace le numéro par `PORT`.

**Méthode :**
1. Copie le script dans un fichier de travail personnel ou exécute-le depuis le terminal.
2. Saisis un port local que tu as observé.
3. Lis les lignes du programme et relie-les aux données reçues.
4. Ne publie ni la bannière complète ni une réponse de challenge dans ce fichier.

**Observe et note :** le service envoie-t-il un texte spontanément ? Quelles informations générales une bannière pourrait-elle divulguer ? Quelle mesure limiterait cette divulgation ?

<details>
<summary>Indice 1</summary>

Le programme se connecte à `127.0.0.1`, lit un nombre limité d'octets, puis les décode en texte.
</details>

<details>
<summary>Indice 2</summary>

Si la connexion fonctionne mais que le texte est vide, le service peut simplement ne pas envoyer de bannière spontanément.
</details>

## Level 3 — Challenge

**But :** réunir scan, identification et lecture d'une bannière sans exposer de réponse.

**Énoncé :** identifie un service sur la cible du lab, puis détermine si sa bannière révèle des détails qui ne devraient pas être publics. Reste sur `127.0.0.1`.

**Méthode :** commence par une plage limitée, vérifie l'état, puis utilise une méthode adaptée au service trouvé. Sous WSL 1, écarte les résultats qui semblent appartenir à Windows.

**Observe et note :** note ta démarche, les options utilisées et une recommandation de protection dans tes notes personnelles. Le fichier du dépôt ne doit contenir ni flag ni solution.

<details>
<summary>Indice 1</summary>

`-sV` peut aider à identifier un service. Une connexion TCP simple peut ensuite permettre d'observer ce que le service envoie.
</details>

<details>
<summary>Indice 2</summary>

Une bannière trop détaillée peut être réduite ou supprimée dans la configuration du service. Distingue l'observation de la conclusion de sécurité.
</details>
