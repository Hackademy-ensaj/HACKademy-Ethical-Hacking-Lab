# 03 — Sécurité web (bases HTTP)

## Level 1 — Learn
Requête / réponse, méthodes GET/POST, codes (200, 401, 404), en-têtes.
```bash
curl -i http://127.0.0.1:8080/admin                                     # formulaire
curl -i -X POST -d "user=test&pass=test" http://127.0.0.1:8080/admin    # 401
```
Vulnérabilités vues ici :
- **Information disclosure** : commentaires, `robots.txt`, fichiers de sauvegarde exposés.
- **Identifiants par défaut** : `admin/admin`, `admin/admin123`…
- **Absence de limitation de tentatives** (brute force possible).

## Level 2 — Practice
1. Liste les chemins de `robots.txt` et visite-les avec `curl`.
2. Trouve le fichier de sauvegarde exposé et lis-le.
3. Teste 5 identifiants courants sur `/admin` avec `curl -X POST`.

## Level 3 — Challenge
Obtiens l'accès admin et récupère le flag. Explique en 3 lignes comment le corriger (à reprendre dans le rapport du module 05).
