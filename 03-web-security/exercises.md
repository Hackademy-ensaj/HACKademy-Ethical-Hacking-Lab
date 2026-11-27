# Exercices — Sécurité web

## Level 2 — Practice

Ces exercices ciblent uniquement le serveur du lab sur `127.0.0.1:8080`. N'essaie les identifiants que sur ce serveur local. Aucun identifiant, mot de passe ou flag trouvé ne doit être ajouté à ce fichier ni à un autre fichier partagé.

### Exercice 1 — Visiter les chemins signalés par `robots.txt`
**But :** comprendre que les directives de `robots.txt` sont publiques et ne constituent pas un contrôle d'accès.

**Énoncé :** lis `robots.txt`, puis visite directement chacun des chemins qu'il mentionne, sur le serveur local. Note les codes de statut et décris les types de réponse obtenus sans divulguer d'information sensible.

**Méthode :**
1. Vérifie que le serveur du lab fonctionne.
2. Lis `http://127.0.0.1:8080/robots.txt` avec `curl -i`.
3. Pour chaque chemin indiqué dans le fichier, envoie une requête `curl -i` à `http://127.0.0.1:8080` suivie de ce chemin.
4. Note les chemins consultés, les statuts et les catégories d'information accessibles. Ne copie aucun secret dans le dépôt.

**Observe et note :** un chemin `Disallow` est-il réellement protégé ? Quelle mesure côté serveur empêcherait l'accès non autorisé ?

### Exercice 2 — Lire la sauvegarde exposée
**But :** examiner l'impact d'un fichier de sauvegarde accessible publiquement.

**Énoncé :** à partir des chemins découverts à l'exercice précédent, consulte la sauvegarde exposée sur le serveur local. Décris quelles catégories d'information elle révèle et pourquoi cette exposition présente un risque. Ne recopie ni empreinte ni mot de passe dans le dépôt.

**Méthode :**
1. Suis les chemins observés dans `robots.txt` et dans les réponses du serveur.
2. Demande le fichier de sauvegarde avec `curl -i` à la cible `127.0.0.1:8080`.
3. Identifie le compte de service et la nature de l'empreinte sans écrire leurs valeurs dans les fichiers partagés.
4. Propose une correction : retirer la sauvegarde de la racine publique et appliquer des contrôles d'accès serveur.

### Exercice 3 — Cinq essais d'identifiants dans le lab local
**But :** observer la validation côté serveur et réfléchir aux protections contre les tentatives répétées.

**Énoncé :** effectue au maximum cinq essais d'identifiants sur le formulaire du lab `http://127.0.0.1:8080/admin`. Ces essais sont autorisés **uniquement sur `127.0.0.1`**. N'utilise pas ces identifiants sur un autre système et n'automatise pas de tentatives supplémentaires.

**Méthode :**
1. Prépare cinq combinaisons au plus pour l'exercice et garde-les dans tes notes privées.
2. Envoie chaque essai au formulaire local en utilisant les champs `user` et `pass`.
3. Observe les codes de statut et le comportement de la réponse ; arrête-toi après cinq essais.
4. Note le nombre d'essais et recommande une limite de tentatives, un délai progressif, des mots de passe uniques et la suppression des identifiants par défaut.

**Observe et note :** le serveur distingue-t-il une authentification acceptée d'un refus ? Pourquoi cinq essais contrôlés dans ce lab ne justifient-ils pas des tentatives sur des comptes ou machines tiers ? Ne publie ni identifiants ni résultat de connexion.

## Level 3 — Challenge

L'objectif du challenge est de retrouver l'accès administrateur du lab local, de récupérer le flag affiché après authentification et de proposer une correction. Limite toutes les requêtes à `127.0.0.1`. Ne mets ni les identifiants ni le flag dans les fichiers du dépôt ; conserve tes réponses dans tes notes personnelles.
