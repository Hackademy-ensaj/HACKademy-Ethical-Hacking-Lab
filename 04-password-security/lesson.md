# 04 — Sécurité des mots de passe

## Level 1 — Learn

### Objectifs
À la fin de cette leçon, tu sauras distinguer hachage et chiffrement, expliquer pourquoi MD5 ne convient pas au stockage des mots de passe, décrire le rôle d'un sel, comparer le principe de bcrypt et Argon2, estimer un espace de recherche et compléter un petit script de vérification de candidats.

### Prérequis
Tu dois savoir ouvrir un terminal et lire quelques lignes de Python. Une chaîne de caractères est du texte entre guillemets. Une variable donne un nom à une valeur.

### Hachage et chiffrement
- **Hachage (hashing) :** transformation d'une donnée en une empreinte de taille définie. On ne récupère pas directement le texte d'origine à partir de l'empreinte.
- **Chiffrement (encryption) :** transformation réversible avec une clé ; la clé permet de retrouver le texte.
- **Analogie :** le hachage ressemble à une empreinte de document ; le chiffrement ressemble à une boîte fermée dont la clé ouvre le contenu.
- **Non injectif :** plusieurs entrées différentes peuvent, en théorie, donner la même empreinte. Une empreinte ne prouve donc pas de manière parfaite quel était le texte original.
- **Pourquoi en sécurité :** on stocke généralement des vérificateurs de mot de passe plutôt que les mots de passe eux-mêmes. On ne doit pas confondre cela avec du chiffrement réversible.
- **Exemple :** un programme calcule une empreinte pour une valeur candidate et la compare à une empreinte de référence, sans afficher ni révéler le mot de passe recherché.

### MD5, sel, bcrypt et Argon2
- **MD5 :** ancienne fonction de hachage, très rapide et aujourd'hui déconseillée pour stocker des mots de passe. Sa rapidité facilite les essais répétés.
- **Sel (salt) :** valeur aléatoire unique ajoutée au mot de passe avant le calcul. Analogie : une pincée différente ajoutée à chaque recette. Le sel n'est pas un secret ; il empêche notamment que deux mots de passe identiques aient le même résultat stocké.
- **bcrypt et Argon2 :** fonctions conçues pour le stockage de mots de passe. Elles permettent de régler un coût de calcul et rendent les essais en masse plus coûteux. Argon2 peut aussi utiliser la mémoire.
- **Pourquoi en sécurité :** un stockage lent et correctement paramétré réduit le nombre d'essais possibles après une fuite. Il ne rend pas un mot de passe faible invulnérable.
- **Exemple de calcul illustratif :** le programme peut calculer l'empreinte MD5 d'un exemple neutre comme `bonjour`. Ne réutilise jamais un mot de passe réel dans une démonstration publique.

### Wordlist et espace de recherche
- **Wordlist (liste de mots) :** fichier contenant des candidats que l'on peut comparer dans un exercice autorisé. Analogie : une liste d'essais possibles.
- Pour des caractères choisis au hasard, si chaque position peut prendre `a` valeurs et que le mot de passe a `n` positions, le nombre de possibilités est `a^n`.
- Avec 26 lettres minuscules et 8 positions : `26^8 = 208 827 064 576` possibilités. À `10^10` essais par seconde, le calcul théorique est d'environ `20,9` secondes.
- Avec 62 caractères possibles et 12 positions : `62^12 ≈ 3,23 × 10^21` possibilités. À `10^10` essais par seconde, cela représente environ `10 200` ans.
- Ces durées sont des estimations pour un tirage aléatoire et un débit hypothétique constant. Le débit réel varie selon le matériel et la fonction utilisée. Une wordlist ou un mot de passe prévisible change complètement l'estimation.

### Script Python à compléter — méthode principale
Ce script parcourt une liste fournie avec le lab et compare les empreintes. Il ne doit être utilisé que sur les fichiers du lab. Les deux blancs sont à compléter ; aucun résultat n'est affiché ici.

```python
import hashlib

empreinte_cible = input("Empreinte de l'exercice : ").strip().lower()
with open("wordlist.txt", encoding="utf-8") as fichier:
    for ligne in fichier:
        candidat = ligne.strip()
        empreinte = hashlib.________(candidat.encode()).hexdigest()
        if empreinte == ________:
            print("Candidat correspondant trouvé dans le fichier local.")
            break
```

Explication, ligne par ligne :
- `import hashlib` charge les fonctions de hachage de la bibliothèque standard.
- `empreinte_cible = input(...).strip().lower()` demande une empreinte, enlève les espaces au début et à la fin, puis normalise les lettres en minuscules.
- `open("wordlist.txt", encoding="utf-8")` ouvre le fichier local en lecture avec l'encodage UTF-8.
- `for ligne in fichier` lit le fichier une ligne à la fois.
- `candidat = ligne.strip()` retire le retour à la ligne autour du candidat.
- La ligne avec le premier blanc calcule l'empreinte du candidat avec la fonction appropriée.
- La condition avec le second blanc compare cette empreinte à la variable contenant la référence.
- `print(...)` indique seulement qu'une correspondance a été trouvée ; le script n'affiche pas le candidat.
- `break` arrête la boucle après une correspondance.

**Erreurs fréquentes :**
- `FileNotFoundError` : lance le script depuis le dossier contenant `wordlist.txt`, ou indique le bon chemin local.
- `AttributeError` : vérifie le nom de la fonction de hachage demandé dans l'exercice.
- Aucune correspondance : le candidat peut ne pas être dans le fichier, l'empreinte peut ne pas correspondre ou le format peut être différent.
- Erreur de comparaison : vérifie la normalisation en minuscules et les espaces autour de l'empreinte.

### John, facultatif
John the Ripper est un outil de test de mots de passe. Il est facultatif : le script Python reste la méthode principale de la leçon. Pour des empreintes MD5 brutes, `--format=raw-md5` demande une version **Jumbo** de John ; certaines versions empaquetées ne proposent pas ce format.

```bash
john --format=raw-md5 --wordlist=wordlist.txt hashes.txt
```

- `john` lance l'outil.
- `--format=raw-md5` indique le format d'empreinte attendu.
- `--wordlist=wordlist.txt` choisit le fichier de candidats.
- `hashes.txt` est le fichier d'empreintes du lab.

Cette commande sert à comprendre le rôle des outils, pas à publier une réponse. N'utilise aucun fichier ou compte qui ne t'appartient pas ou pour lequel tu n'as pas d'autorisation.

**Erreur fréquente :** si John indique que `raw-md5` est inconnu, vérifie la version installée ; le format demande la version Jumbo. Tu peux poursuivre avec le script Python de l'exercice.

### Comment se protéger
- Ne stocke jamais les mots de passe en clair ni avec MD5.
- Utilise une fonction adaptée comme Argon2id ou bcrypt, un sel aléatoire unique et des paramètres de coût maintenus à jour.
- Encourage des mots de passe longs, uniques et difficiles à deviner ; propose un gestionnaire de mots de passe.
- Protège les fichiers d'empreintes et limite les accès.
- Active une authentification multifacteur lorsque c'est possible.

## Level 2 — Practice
Complète les deux blancs du script dans un fichier personnel, puis teste-le seulement avec les fichiers d'exercice fournis. N'ajoute aucun mot de passe, candidat ou réponse dans les fichiers Markdown du dépôt. John est facultatif.

## Level 3 — Challenge
Étudie les empreintes fournies par le lab et explique pourquoi un stockage rapide sans sel est risqué. Rédige une recommandation défensive. Ne publie aucun mot de passe, résultat trouvé ou corrigé dans les fichiers Markdown.

## Résumé
- Le hachage n'est pas un chiffrement réversible.
- MD5 est trop rapide et inadapté au stockage des mots de passe.
- Un sel unique limite la réutilisation des mêmes empreintes.
- bcrypt et Argon2 sont conçus pour rendre les essais plus coûteux.
- `a^n` estime le nombre de candidats aléatoires ; les durées réelles varient.
- Un script peut comparer des candidats localement. John est facultatif et `raw-md5` demande la version Jumbo.

### Mini-quiz
1. Le chiffrement est-il réversible avec une clé ?
2. À quoi sert un sel unique ?
3. Combien de possibilités y a-t-il pour 26 caractères possibles à chacune de 8 positions ?
4. Pourquoi MD5 est-il déconseillé pour stocker des mots de passe ?

<details>
<summary>Afficher les réponses</summary>

1. Oui, avec la clé appropriée.
2. Il rend les empreintes distinctes même si deux utilisateurs ont le même mot de passe et complique les attaques pré-calculées.
3. `26^8`, soit `208 827 064 576` possibilités.
4. Il est très rapide et facilite les essais répétés ; il n'est pas conçu pour le stockage des mots de passe.
</details>
