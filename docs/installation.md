# Installation (WSL 1)
1. Windows : activer WSL, installer **Ubuntu** depuis le Microsoft Store. Vérifier la version dans PowerShell : `wsl -l -v` (VERSION = 1).
2. Ouvrir Ubuntu, puis :
```bash
git clone https://github.com/Hackademy-ensaj/HACKademy-Ethical-Hacking-Lab.git
cd HACKademy-Ethical-Hacking-Lab
bash setup.sh
bash start-target.sh
```
3. Vérifier dans un 2e terminal : `curl -I http://127.0.0.1:8080`

## Problèmes fréquents
- `nmap` erreur raw socket → ajouter `-sT -Pn`.
- Port déjà utilisé → Ctrl+C sur l'ancien terminal ou `pkill -f server.py`.
- `apt update` échoue → `sudo apt update --fix-missing`.
