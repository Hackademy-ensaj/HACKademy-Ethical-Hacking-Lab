# 01 — Reconnaissance

## Level 1 — Learn
La reconnaissance = collecter de l'information **avant** d'attaquer. Deux types :
- **Passive** : sans toucher la cible (DNS public, WHOIS).
- **Active** : interaction directe (requêtes HTTP, scan).

Démos :
```bash
dig scanme.nmap.org A +short        # adresse IP
dig nmap.org MX +short              # serveurs mail
dig nmap.org NS +short              # serveurs de noms
curl -I http://scanme.nmap.org      # en-têtes HTTP (serveur, technologies)
curl -s http://127.0.0.1:8080/robots.txt
```
Ce qu'on cherche : technologies, versions, chemins cachés (`robots.txt`), commentaires dans le code source.
