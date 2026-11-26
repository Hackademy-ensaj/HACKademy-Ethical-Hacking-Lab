# 04 — Sécurité des mots de passe

## Level 1 — Learn
Un hash n'est pas chiffré : on ne le « déchiffre » pas, on **teste des candidats** et on compare.
MD5 = rapide = faible pour stocker des mots de passe (utiliser bcrypt/argon2 + sel).
```bash
echo -n "password" | md5sum
```

## Level 2 — Practice (John, facultatif)
```bash
cd challenges
john --format=raw-md5 --wordlist=wordlist.txt hashes.txt
john --format=raw-md5 --show hashes.txt
```
Sans John : écris un script Python qui hash chaque mot de `wordlist.txt` et compare.

## Level 3 — Challenge
Le hash de `svc_backup` (trouvé dans `/backup/notes.txt`) : retrouve son mot de passe et explique pourquoi MD5 est un mauvais choix.
