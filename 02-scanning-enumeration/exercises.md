# Exercices — Scan et énumération

## Level 2 — Practice

Tous les scans de cette section sont limités à `127.0.0.1`, sauf l'exercice 3 qui utilise uniquement `scanme.nmap.org` avec le scan rapide demandé. Vérifie que le serveur du lab tourne avant de commencer. Sous WSL 1, certains ports visibles peuvent appartenir à Windows et non au lab : consigne cette limite dans tes observations.

### Exercice 1 — Compter les ports du lab
**But :** établir quels ports TCP du lab sont accessibles dans la plage demandée et compter les ports ouverts observés.

**Énoncé :** scanne les ports de `1` à `10000` sur `127.0.0.1`. Relève le nombre de ports marqués `open` et leurs numéros. Le résultat dépend de ton environnement ; n'inscris pas un nombre supposé dans le dépôt.

**Méthode :**
1. Lance la cible locale dans un autre terminal et laisse-la fonctionner.
2. Exécute `nmap -sT -Pn -p 1-10000 127.0.0.1`.
3. Compte uniquement les lignes dont l'état est `open`, sans confondre les ports `closed` ou `filtered` avec des ports ouverts.
4. Note la commande, le nombre compté et tout résultat qui pourrait venir de Windows sous WSL 1.

**Observe et note :** quelle plage a été testée ? Que signifie exactement `open` ? Pourquoi le résultat d'un scan ne prouve-t-il pas qu'un service est vulnérable ?

<details>
<summary>Indice 1</summary>

La plage est donnée par `-p 1-10000`. `-sT` utilise une connexion TCP complète et `-Pn` évite l'étape préalable de détection par ping.
</details>

<details>
<summary>Indice 2</summary>

Compte les lignes `open` du tableau des ports. Un port ouvert indique qu'une application répond ; il ne constitue pas à lui seul un constat de vulnérabilité.
</details>

### Exercice 2 — Lire une bannière du lab
**But :** observer le texte envoyé par le service local et repérer les informations éventuellement divulguées.

**Énoncé :** identifie les ports locaux, puis utilise le client Python de la leçon sur le port TCP de la bannière du lab. Lis la bannière et décris ce qu'elle révèle sans recopier son flag dans ce fichier ni dans tes notes partagées.

**Méthode :**
1. Vérifie que le service du lab est démarré sur `127.0.0.1`.
2. Lance le client Python présenté dans la leçon et saisis le port local identifié pour le service de bannière.
3. Observe le texte reçu et distingue le nom du service, les détails de version et les autres éléments.
4. Dans tes notes personnelles, explique pourquoi une bannière trop détaillée peut augmenter le risque et propose une mesure de réduction de l'information divulguée.

**Observe et note :** le texte est-il envoyé spontanément à la connexion ? Quelles catégories d'information y figurent ? Ne publie pas la bannière complète ni la réponse du challenge.

### Exercice 3 — Scan rapide de `scanme.nmap.org`
**But :** comprendre le périmètre d'un scan rapide et modéré sur l'hôte de démonstration explicitement autorisé par le projet Nmap.

**Énoncé :** effectue uniquement le scan rapide `-F` demandé sur `scanme.nmap.org`. N'ajoute pas d'autres options de scan et ne lance pas de scan étendu sur cet hôte.

**Méthode :**
1. Exécute `nmap -F scanme.nmap.org` une seule fois.
2. Lis les ports et états retournés, si le service est disponible.
3. Note que le résultat dépend du moment, du réseau et de la configuration de la cible ; il peut évoluer.

**Observe et note :** que fait l'option `-F` ? En quoi le périmètre diffère-t-il d'un scan de tous les ports ? N'interprète pas un résultat observé comme une autorisation de tester d'autres hôtes.

## Level 3 — Challenge

**But :** retrouver le flag présent dans la bannière du service du lab, puis expliquer quelle information la bannière divulgue et proposer une correction défensive.

**Énoncé :** utilise les observations de scan et la méthode de lecture de bannière pour trouver le flag de la bannière sur `127.0.0.1` uniquement. Décris ensuite une correction qui réduirait ou supprimerait les détails sensibles de la bannière. Ne publie pas la valeur du flag ni la bannière complète dans les fichiers du dépôt.

**Méthode :** identifie un port ouvert du lab, connecte-toi au service local approprié, examine le texte reçu et formule une recommandation de configuration. Sous WSL 1, vérifie que le port observé appartient bien au lab.

**Observe et note :** garde le flag uniquement dans tes notes personnelles, avec la commande, les observations et la correction proposée. N'effectue aucun essai d'identifiants sur `scanme.nmap.org` ni sur une autre machine.
