# 03 — Sécurité web : bases HTTP

## Level 1 — Learn

### Objectifs
À la fin de cette leçon, tu sauras décrire une requête et une réponse HTTP, distinguer GET et POST, reconnaître les codes 200, 401 et 404, comprendre les formulaires et expliquer les risques d'une divulgation d'information, d'identifiants faibles et d'une absence de limite de tentatives.

### Prérequis
Tu dois savoir lancer le serveur local. Une adresse comme `http://127.0.0.1:8080/` contient le protocole (`http`), l'adresse (`127.0.0.1`), le port (`8080`) et le chemin (`/`). La cible d'exercice est uniquement ta machine locale.

### Requête, réponse et formulaire
- **Requête HTTP :** message envoyé par le client pour demander une page ou transmettre des données. Analogie : remplir un bon de commande.
- **Réponse HTTP :** message du serveur qui indique le résultat et peut contenir une page. Analogie : le reçu ou la réponse du magasin.
- **Formulaire :** éléments d'une page qui permettent de saisir et transmettre des données. Un formulaire de connexion envoie un nom d'utilisateur et un mot de passe.
- **Pourquoi en sécurité :** une application doit vérifier les données reçues côté serveur. Masquer un champ dans la page ne suffit pas.

### GET et POST
- **GET :** demande une ressource. Les paramètres peuvent apparaître dans l'adresse. Analogie : demander le contenu d'une page.
- **POST :** transmet des données dans le corps de la requête. Analogie : envoyer un formulaire rempli au guichet.
- **Pourquoi en sécurité :** POST ne chiffre pas les données à lui seul. En production, HTTPS protège le transport ; le serveur doit aussi vérifier les données et protéger les comptes.
- **Exemple sûr :** envoyer une valeur factice à la page locale pour observer le code de réponse, sans essayer de deviner des identifiants.

### Codes HTTP
- **200 :** la requête a été traitée avec succès.
- **401 :** la ressource demande une authentification, ou l'authentification fournie n'est pas acceptée.
- **404 :** la ressource demandée n'a pas été trouvée.
- **Analogie :** 200 = demande servie ; 401 = accès à vérifier ; 404 = adresse inconnue.
- **Pourquoi en sécurité :** les codes aident à comprendre le comportement. Des messages trop précis peuvent aussi révéler des détails ; un code seul ne prouve pas une vulnérabilité.

### `curl` pour lire une page et soumettre un formulaire factice
```bash
curl -i http://127.0.0.1:8080/admin
curl -i -X POST -d "user=exemple&pass=valeur-factice" http://127.0.0.1:8080/admin
```

Explication de chaque élément :
- `curl` : client qui envoie une requête HTTP.
- `-i` : affiche les en-têtes de réponse et le contenu.
- `-X POST` : choisit la méthode POST. `-X` est suivi du nom de méthode.
- `-d "..."` : ajoute des données de formulaire au corps de la requête. Ici les valeurs sont factices et ne sont pas des identifiants à tester.
- `http://127.0.0.1:8080/admin` : cible locale et chemin du formulaire.

**Sortie illustrative, pas une réponse réelle :**
```text
HTTP/1.0 [code et texte de statut]
Content-Type: [type]

[contenu ou message de réponse]
```
Lis d'abord la ligne de statut, puis les en-têtes. Après la ligne vide vient le contenu. Une soumission factice peut recevoir un refus ; le code exact dépend du traitement du serveur.

**Erreurs fréquentes :**
- `Failed to connect` : lance le serveur local et vérifie l'adresse et le port.
- `404` : vérifie le chemin demandé. Cela ne veut pas dire que tous les chemins sont inexistants.
- `401` : le serveur refuse l'authentification ou demande une authentification. Ne cherche pas à contourner cette vérification hors d'un exercice explicitement autorisé.
- `curl -I` retourne une erreur 501 sur ce serveur : il ne gère pas HEAD. Utilise `curl -i`.
- Données mal formées : vérifie les noms de champs et le séparateur `&`. N'envoie que des valeurs factices dans cet exemple.

### Faiblesses observées dans un audit
- **Divulgation d'information (information disclosure) :** publication accidentelle d'informations internes. Analogie : laisser un dossier de travail sur le comptoir. Des commentaires, des fichiers de sauvegarde ou des listes de chemins peuvent en être la cause.
- **Identifiants faibles ou par défaut :** secrets faciles à deviner ou laissés avec une valeur initiale. Analogie : une clé identique pour toutes les portes.
- **Force brute (brute force) :** répétition automatisée de nombreuses tentatives d'authentification. Analogie : essayer beaucoup de clés une par une.
- **Pourquoi en sécurité :** ces erreurs peuvent exposer des données ou un compte. Une vérification doit se faire seulement dans le lab et sans chercher ni divulguer de mot de passe.

### Comment se protéger
- Retire du site de production les commentaires, sauvegardes et documents internes.
- Utilise des mots de passe uniques et robustes ; supprime les identifiants par défaut avant la mise en service.
- Mets une limite de tentatives, ajoute un délai progressif et surveille les échecs répétés.
- Protège les sessions, applique une authentification côté serveur et utilise HTTPS.
- Retourne des messages d'erreur utiles mais qui ne révèlent pas si un compte existe.

## Level 2 — Practice
Dans le lab local, observe le formulaire et les codes de réponse avec les valeurs factices ci-dessus. Décris la requête et la réponse sans essayer de deviner un identifiant. Tu peux examiner les ressources explicitement prévues par le lab, mais ne copie aucun secret dans les fichiers Markdown.

## Level 3 — Challenge
Réalise une revue défensive des faiblesses web intentionnelles de la cible locale. Pour chaque observation, explique son impact et propose une correction. Le but est de comprendre le risque, pas de publier des identifiants ni de fournir un corrigé.

## Résumé
- Le client envoie une requête HTTP ; le serveur renvoie une réponse.
- GET demande une ressource ; POST transmet des données dans le corps.
- 200, 401 et 404 décrivent des résultats différents.
- Une information exposée, des identifiants faibles et les tentatives sans limite sont des risques.
- Les corrections se font côté serveur et dans la configuration, pas seulement dans la page affichée.

### Mini-quiz
1. Où se trouvent généralement les données ajoutées avec `curl -d` ?
2. Que signifie généralement une réponse 404 ?
3. POST chiffre-t-il à lui seul les données ?
4. Cite une mesure qui limite les tentatives répétées.

<details>
<summary>Afficher les réponses</summary>

1. Dans le corps de la requête.
2. La ressource demandée n'a pas été trouvée.
3. Non. Il faut HTTPS pour chiffrer le transport.
4. Par exemple, limiter les tentatives ou appliquer un délai progressif.
</details>
