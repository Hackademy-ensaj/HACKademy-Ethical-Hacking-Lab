# 02 — Scan et énumération

## Level 1 — Learn

### Objectifs
À la fin de cette leçon, tu sauras expliquer ce qu'est un port et un service, interpréter les états `open`, `closed` et `filtered`, lancer un scan limité avec `nmap`, lire une bannière et comprendre un petit client TCP écrit avec `socket`.

### Prérequis
Tu dois savoir ouvrir un terminal et lancer la cible locale comme indiqué dans le guide d'installation. `127.0.0.1` désigne ta propre machine. Ne scanne que `127.0.0.1` et, avec modération, `scanme.nmap.org`.

### Port, service et états
- **Port :** numéro logique associé à une communication réseau. Analogie : le numéro d'un appartement dans un immeuble.
- **Service :** programme qui attend des demandes sur un port. Analogie : le bureau qui reçoit les visiteurs à cette porte.
- **Pourquoi en sécurité :** un service accessible peut contenir une erreur de configuration ou un défaut. Il faut savoir ce qui est exposé, dans un périmètre autorisé.
- **`open` (ouvert) :** une application répond sur ce port.
- **`closed` (fermé) :** la machine répond, mais aucune application n'accepte la connexion sur ce port.
- **`filtered` (filtré) :** un pare-feu ou un équipement empêche de déterminer l'état avec certitude.
- **Exemple :** un port ouvert indique qu'un service répond, pas qu'il est vulnérable.

### `nmap`
`nmap` est un outil qui vérifie des ports et peut essayer d'identifier les services. Sous WSL 1, utilise souvent `-sT -Pn`. WSL 1 peut aussi afficher des ports de Windows : vérifie que le service répond bien depuis la cible attendue avant de conclure.

```bash
nmap -sT -Pn 127.0.0.1
nmap -sT -Pn -p 1-1000 127.0.0.1
nmap -sT -Pn -p- 127.0.0.1
nmap -sT -Pn -sV -p 1-1000 127.0.0.1
nmap -sT -Pn --script http-headers -p 1-1000 127.0.0.1
nmap -sT -Pn -F scanme.nmap.org
```

Explication des options et arguments :
- `nmap` : lance le scanner.
- `-sT` : utilise une connexion TCP complète pour tester les ports. C'est souvent compatible avec WSL 1.
- `-Pn` : ne fait pas d'étape préalable de détection par ping ; traite l'hôte comme actif. Cela ne rend pas le scan invisible.
- `-p 1-1000` : teste la plage de ports indiquée. `-p` introduit les ports ; `1-1000` est une plage illustrative, pas une liste des ports du lab.
- `-p-` : teste tous les ports TCP. Cela prend plus de temps ; utilise-le seulement sur la cible autorisée.
- `-sV` : demande à `nmap` d'essayer d'identifier les services et leurs versions.
- `--script http-headers` : lance le script NSE nommé `http-headers`, conçu pour lire des en-têtes HTTP. Un script peut envoyer des requêtes supplémentaires.
- `-F` : scan rapide d'un ensemble réduit de ports courants.
- `127.0.0.1` et `scanme.nmap.org` : cibles. Ne remplace pas ces valeurs par une machine non autorisée.

**Sortie illustrative, pas une sortie réelle du lab :**
```text
PORT    STATE     SERVICE
[NUMÉRO]/tcp  [open|closed|filtered]  [nom estimé]
```
- `PORT` indique le numéro et le protocole.
- `STATE` indique l'état observé. `open`, `closed` et `filtered` ne signifient pas la même chose.
- `SERVICE` est une estimation du nom du service. Sans `-sV`, cette estimation peut venir uniquement du numéro de port.
- Avec `-sV`, `nmap` peut afficher une version estimée. Une estimation n'est pas une preuve absolue.

**Erreurs fréquentes :**
- Erreur de socket brut ou de privilèges sous WSL 1 : essaie `-sT -Pn`.
- Scan sans résultat : vérifie que la cible locale est lancée, puis vérifie la plage demandée.
- Résultats inattendus sous WSL 1 : des ports de Windows peuvent apparaître. Ne les attribue pas automatiquement au programme du lab.
- Scan trop long : commence avec une plage limitée ou `-F`, uniquement dans le périmètre permis.

### Bannière
- **Définition :** texte envoyé par un service pour s'identifier ou accueillir une connexion.
- **Analogie :** une enseigne à l'entrée d'un magasin.
- **Pourquoi en sécurité :** une bannière trop bavarde peut révéler le logiciel ou sa version et aider à cibler une attaque.
- **Exemple :** une connexion à un service TCP peut recevoir une ligne de texte avant toute autre commande. Dans les explications, le numéro du service est écrit `PORT` pour ne pas révéler la réponse d'un exercice.

Pour le service HTTP local, `curl -i http://127.0.0.1:8080/` affiche la réponse HTTP. Pour lire une bannière TCP générique, le client Python ci-dessous se connecte uniquement à la boucle locale.

### Client Python avec `socket`, ligne par ligne
```python
import socket

HOTE = "127.0.0.1"
PORT = int(input("Port autorisé à tester : "))
connexion = socket.create_connection((HOTE, PORT), timeout=3)
banniere = connexion.recv(200)
print(banniere.decode(errors="replace"))
connexion.close()
```

- `import socket` charge la bibliothèque réseau standard de Python.
- `HOTE = "127.0.0.1"` fixe la destination à la machine locale. Ne remplace pas cette valeur par un hôte tiers.
- `input(...)` demande le port à tester ; `int(...)` transforme le texte saisi en nombre.
- `socket.create_connection((HOTE, PORT), timeout=3)` ouvre une connexion TCP vers cette adresse et attend au plus trois secondes.
- `connexion.recv(200)` lit jusqu'à 200 octets reçus. La bannière peut être plus courte.
- `.decode(errors="replace")` transforme les octets en texte ; les octets qui ne sont pas décodables sont remplacés.
- `print(...)` affiche le texte reçu.
- `connexion.close()` ferme proprement la connexion.

**Sortie illustrative, pas une réponse réelle :**
```text
[texte envoyé par le service, s'il en envoie un]
```
Une sortie vide peut indiquer que le service n'envoie pas de bannière spontanée, ou que la connexion a été fermée. Une erreur de délai indique qu'aucune donnée n'a été reçue dans le temps prévu.

**Erreurs fréquentes :**
- `ConnectionRefusedError` : aucun service n'accepte la connexion à cette adresse et à ce port, ou la cible n'est pas lancée.
- `TimeoutError` : la connexion n'a pas abouti à temps ; vérifie la cible et l'état du service.
- `ValueError` : le port saisi n'est pas un nombre. Saisis un numéro de port autorisé.
- Le port est ouvert mais aucune bannière n'apparaît : tous les services n'en envoient pas une automatiquement.

### Comment se protéger
- Ferme les services et ports qui ne sont pas nécessaires.
- Mets à jour les services et limite les connexions avec un pare-feu.
- Masque les détails de version qui ne sont pas utiles aux utilisateurs.
- Surveille les scans inattendus et vérifie l'origine des ports observés, notamment sous WSL 1.
- N'effectue pas de scan hors du périmètre autorisé.

## Level 2 — Practice
Suis les exercices de [`exercises.md`](exercises.md). Commence par un scan limité sur la cible locale. Note la commande, l'état des ports et les limites de l'observation.

## Level 3 — Challenge
Sur la cible locale uniquement, observe un service qui envoie une bannière. Explique ce que le texte permet de savoir et propose une mesure de réduction du risque. Ne publie pas la bannière ni la solution dans un fichier Markdown.

## Résumé
- Un port est une porte logique ; un service est le programme qui l'utilise.
- `open`, `closed` et `filtered` décrivent des états différents.
- `nmap` teste des ports. Chaque option change le type ou l'étendue du test.
- Une bannière peut donner des renseignements, mais tous les services n'en envoient pas.
- Sous WSL 1, des ports Windows peuvent apparaître.

### Mini-quiz
1. Un port `filtered` prouve-t-il que le service est arrêté ?
2. Que change `-sV` ?
3. Que teste `-p-` ?
4. Pourquoi faut-il faire attention aux bannières ?

<details>
<summary>Afficher les réponses</summary>

1. Non. Le filtrage empêche de déterminer l'état avec certitude.
2. `nmap` tente d'identifier les services et leurs versions.
3. Tous les ports TCP.
4. Elles peuvent révéler des détails sur le logiciel ou sa version.
</details>
