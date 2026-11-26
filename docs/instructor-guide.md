# Guide formateur (corrections)
| Module | Réponse |
|---|---|
| 01 | `X-Powered-By: PythonLab/3` ; `robots.txt` → `/admin`, `/backup/` ; commentaire HTML → `/dev-notes` → `HACK{commentaires_html_bavards}` |
| 02 | Ports 8080 (HTTP) et 2121 (faux FTP) ; bannière 2121 → `HACK{banniere_bavarde}` |
| 03 | `/backup/notes.txt` exposé ; `admin / admin123` → `HACK{identifiants_par_defaut}` |
| 04 | Hash `5f4dcc3b5aa765d61d8327deb882cf99` = `password` ; hashes.txt : letmein, dragon, sunshine, azerty |
| 05 | 3 flags ci-dessus + rapport |

Correctifs attendus : retirer commentaires/fichiers de dev, désactiver les listings, mots de passe forts + limitation de tentatives, bcrypt/argon2, masquer les bannières.
