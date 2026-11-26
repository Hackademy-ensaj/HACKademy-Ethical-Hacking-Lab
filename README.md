# HACKademy Ethical Hacking Lab

Lab d'initiation à l'ethical hacking, **100 % WSL 1**, sans Docker ni Flask.
Tout se fait sur une cible locale (`127.0.0.1`) lancée en une commande.

## Démarrage rapide
```bash
git clone https://github.com/Hackademy-ensaj./HACKademy-Ethical-Hacking-Lab.git
cd HACKademy-Ethical-Hacking-Lab
bash setup.sh          # installe les outils
bash start-target.sh   # lance la cible (laisser ce terminal ouvert)
```
Ouvre un **second terminal WSL** pour les exercices.

## Parcours
| Module | Contenu | Outils |
|---|---|---|
| 01 | Reconnaissance | dig, curl, nmap |
| 02 | Scan et énumération | nmap, curl |
| 03 | Sécurité web | curl |
| 04 | Mots de passe | john (facultatif) |
| 05 | Mini pentest + rapport | tout |

Chaque module : **Learn → Practice → Challenge**.

## Règle d'or
Ne scanner que : `127.0.0.1` (la cible du lab) et `scanme.nmap.org` (autorisé par le projet Nmap, usage raisonnable).
Toute autre machine sans autorisation écrite est **interdite**.

## Limites WSL 1
Utiliser `nmap -sT -Pn` (scan connect). Les scans SYN `-sS`, la détection d'OS `-O` et le ping ICMP brut ne fonctionnent pas.
