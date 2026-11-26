# 02 — Scan et énumération

## Level 1 — Learn
> WSL 1 : toujours `-sT -Pn`.
```bash
nmap -sT -Pn 127.0.0.1                    # 1000 ports courants
nmap -sT -Pn -p 8080,2121 127.0.0.1       # ports précis
nmap -sT -Pn -p- 127.0.0.1                # tous les ports
nmap -sT -Pn -sV -p 8080,2121 127.0.0.1   # versions des services
nmap -sT -Pn --script http-headers -p 8080 127.0.0.1
nmap -sT -Pn -F scanme.nmap.org           # cible externe autorisée
```
États d'un port : `open`, `closed`, `filtered`.
Énumération : une fois un service trouvé, on récupère sa bannière :
```bash
curl -i http://127.0.0.1:8080/
python3 -c "import socket;s=socket.create_connection(('127.0.0.1',2121));print(s.recv(200).decode())"
```
