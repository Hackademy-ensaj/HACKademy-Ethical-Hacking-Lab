# 01 — Reconnaissance

## Level 1 — Learn

### Objectifs
À la fin de cette leçon, tu sauras distinguer la reconnaissance passive et active, lire une adresse IP et des enregistrements DNS, utiliser `dig` et `curl`, puis repérer des informations exposées dans des en-têtes HTTP, `robots.txt` et des commentaires HTML.

### Prérequis
Tu as besoin d'un terminal. Une **commande** est une instruction que tu écris pour demander une action à l'ordinateur. Dans une commande, les mots après le nom du programme sont souvent des options ou des arguments.

### Reconnaissance passive et active
- **Définition :** la reconnaissance passive collecte des informations sans envoyer de requête à la cible. La reconnaissance active contacte directement la cible.
- **Analogie :** lire l'adresse sur une enveloppe est passif ; sonner à la porte est actif.
- **Pourquoi en sécurité :** les informations publiques aident à comprendre l'exposition d'un système. Une requête directe laisse une trace et doit rester dans le périmètre autorisé.
- **Exemple :** demander une information DNS est une consultation ; demander une page web à `127.0.0.1` contacte le serveur local.

### IP et DNS
- **IP (Internet Protocol) :** adresse qui permet d'acheminer des données vers une machine. C'est comme une adresse postale pour le réseau.
- **DNS (Domain Name System) :** annuaire qui associe des noms de domaine à des informations réseau. Il évite de retenir des adresses numériques.
- **A :** associe un nom à une adresse IPv4. **MX :** indique les serveurs qui reçoivent les courriels d'un domaine. **NS :** indique les serveurs qui répondent pour la zone DNS.
- **Pourquoi en sécurité :** les enregistrements donnent des indices sur l'infrastructure. Ils ne donnent pas l'autorisation de tester les machines.
- **Exemple :** une requête DNS peut demander l'enregistrement A de `scanme.nmap.org`.

### `dig`
`dig` signifie « Domain Information Groper ». Il pose une question au DNS et affiche la réponse.

```bash
dig scanme.nmap.org A +short
dig nmap.org MX +short
dig nmap.org NS +short
```

Lecture des arguments, dans l'ordre :
- `dig` : lance l'outil de consultation DNS.
- `scanme.nmap.org`, puis `nmap.org` : nom demandé.
- `A`, `MX` ou `NS` : type d'information demandé.
- `+short` : demande un affichage court. Sans cette option, `dig` montre aussi les détails de la requête et de la réponse.

**Sortie illustrative, pas une réponse réelle :**
```text
[adresse IPv4 retournée par le DNS]
[nom d'un serveur de courrier]
[nom d'un serveur DNS]
```
Chaque ligne correspond à un enregistrement retourné. Une réponse vide peut signifier qu'il n'y a pas d'enregistrement de ce type, ou que le DNS n'a pas répondu comme prévu.

**Erreurs fréquentes :**
- `dig: command not found` : installe `dnsutils` avec le guide d'installation.
- `connection timed out` : vérifie la connexion réseau et réessaie plus tard.
- Mauvais type demandé : vérifie que tu as écrit `A`, `MX` ou `NS` après le nom.

### Client, serveur et HTTP
- **Client :** programme qui demande une ressource. **Serveur :** programme qui répond. Analogie : tu demandes un livre à une bibliothèque ; le comptoir reçoit la demande et te répond.
- **HTTP (Hypertext Transfer Protocol) :** règles utilisées par un client et un serveur pour échanger des pages et des données.
- **Requête :** demande envoyée au serveur. **Réponse :** statut, en-têtes et parfois contenu renvoyés par le serveur.
- **En-tête HTTP :** petite information associée à la requête ou à la réponse, comme le type de contenu. Des en-têtes trop détaillés peuvent révéler des informations techniques.
- **Pourquoi en sécurité :** des détails inutiles aident un observateur à reconnaître un logiciel ou une mauvaise configuration.

### `curl`
`curl` envoie des requêtes réseau et affiche la réponse. Dans ce lab, contacte seulement `127.0.0.1`; `scanme.nmap.org` est réservé aux vérifications autorisées et modérées.

```bash
curl -i http://127.0.0.1:8080/
curl -s http://127.0.0.1:8080/robots.txt
curl -I http://scanme.nmap.org
```

Explication des éléments :
- `curl` : lance le client HTTP.
- `-i` : affiche les en-têtes de réponse puis le contenu.
- `-s` : mode silencieux, qui masque notamment la barre de progression. Il ne rend pas la requête anonyme.
- `-I` : envoie une requête `HEAD`, qui demande les en-têtes sans le contenu. Certains serveurs ne l'acceptent pas. Dans ce dépôt, n'utilise pas `-I` sur la cible locale : son serveur ne gère pas `HEAD` et répond avec une erreur. Utilise `-i` en local.
- `http://...` : adresse de la ressource demandée. `127.0.0.1` désigne la machine locale ; `8080` est le port de l'application du lab.
- `/` ou `/robots.txt` : chemin de la ressource sur le serveur.

**Sortie illustrative, pas une réponse réelle :**
```text
HTTP/1.0 [code et texte de statut]
Content-Type: [type de contenu]

[contenu éventuel de la page]
```
La première ligne indique le statut. Les lignes suivantes sont les en-têtes. Une ligne vide sépare les en-têtes du contenu. Avec `-s`, la réponse reste affichée, mais pas la barre de progression.

**Erreurs fréquentes :**
- `Could not resolve host` : vérifie le nom et le DNS.
- `Failed to connect` : vérifie que la cible autorisée est lancée et que l'adresse est correcte.
- Erreur après `curl -I` en local : c'est attendu pour ce serveur. Remplace `-I` par `-i`.
- Une réponse `404` signifie que le chemin demandé n'existe pas sur le serveur ; cela ne signifie pas que le serveur est arrêté.

### `robots.txt` et commentaires HTML
- `robots.txt` est un fichier de consignes destiné aux robots d'indexation. Analogie : une pancarte qui indique des zones qu'un moteur de recherche devrait éviter. Ce n'est pas un contrôle d'accès : un chemin indiqué peut rester accessible.
- Un commentaire HTML est une note dans le code source, souvent écrite entre `<!--` et `-->`. Analogie : une note laissée dans la marge d'un document.
- **Pourquoi en sécurité :** un fichier ou un commentaire publié par erreur peut révéler des chemins ou des détails internes. Une consigne publique ne remplace jamais une authentification.
- **Exemple :** lire la réponse de `/robots.txt` ou le code HTML de la page d'accueil locale avec `curl -i`.

### Comment se protéger
- Ne publie pas de commentaires internes ni de fichiers de développement dans un site de production.
- Ne place pas de secrets dans `robots.txt` : il est public.
- Limite les en-têtes aux informations réellement utiles.
- Protège les ressources privées par une authentification et des contrôles d'accès côté serveur.
- N'effectue de reconnaissance active que sur une cible autorisée.

## Level 2 — Practice
Suis les exercices de [`exercises.md`](exercises.md). Note les commandes, les observations et les questions. Ne copie pas seulement la sortie : explique ce que chaque élément signifie.

## Level 3 — Challenge
À partir des indices publics disponibles sur la cible locale, cherche une information de développement exposée. Ne teste que `127.0.0.1`. Note ta méthode dans tes notes personnelles, sans publier de secret dans un fichier Markdown du dépôt.

## Résumé
- La reconnaissance passive ne contacte pas directement la cible ; la reconnaissance active la contacte.
- Une IP identifie une destination réseau ; le DNS associe des noms à des informations réseau.
- `dig` demande des enregistrements DNS. `curl` envoie des requêtes HTTP.
- Les en-têtes, `robots.txt` et les commentaires peuvent révéler des informations.
- Une information visible n'est pas une autorisation de tester une autre machine.

### Mini-quiz
1. Quel type d'enregistrement DNS associe un nom à une adresse IPv4 ?
2. Est-ce que `robots.txt` bloque réellement l'accès à une page ?
3. Quelle option de `curl` affiche en-têtes et contenu ?
4. Quelle différence y a-t-il entre une reconnaissance passive et active ?

<details>
<summary>Afficher les réponses</summary>

1. `A`.
2. Non. C'est une consigne publique, pas une protection d'accès.
3. `-i`.
4. La passive n'envoie pas de requête directe à la cible ; l'active la contacte.
</details>
