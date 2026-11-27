#!/usr/bin/env python3
"""Cible pédagogique HACKademy. Écoute UNIQUEMENT sur 127.0.0.1.
HTTP :8080 (site vulnérable volontairement) + faux FTP :2121 (bannière).
Python standard uniquement."""
import socketserver, threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

HOST = "127.0.0.1"

PAGES = {
    "/": "<h1>HACKademy Corp</h1><p>Bienvenue.</p>\n<!-- TODO: retirer /dev-notes avant la mise en prod -->",
    "/robots.txt": "User-agent: *\nDisallow: /admin\nDisallow: /backup/\n",
    "/dev-notes": "Notes dev\nFlag recon: HACK{commentaires_html_bavards}\n",
    "/backup/": "Index of /backup\n - notes.txt\n",
    "/backup/notes.txt": "Compte de service : svc_backup\nHash MD5 : 5f4dcc3b5aa765d61d8327deb882cf99\n",
}
LOGIN = "<h1>Admin</h1><form method='POST'><input name='user'><input name='pass' type='password'><button>Login</button></form>"

class H(BaseHTTPRequestHandler):
    server_version = "HACKademyHTTP/0.1"

    def _send(self, code, body, ctype="text/html"):
        self.send_response(code)
        self.send_header("X-Powered-By", "PythonLab/3")
        self.send_header("Content-Type", ctype + "; charset=utf-8")
        self.end_headers()
        # HEAD doit retourner les mêmes en-têtes que GET, sans envoyer le corps.
        if self.command != "HEAD":
            self.wfile.write(body.encode())

    def do_GET(self):
        p = self.path.split("?")[0]
        if p == "/admin":
            return self._send(200, LOGIN)
        if p in PAGES:
            return self._send(200, PAGES[p], "text/plain" if p != "/" else "text/html")
        self._send(404, "Not found")

    def do_HEAD(self):
        # Réutilise le routage et les en-têtes de GET ; _send omet le corps.
        return self.do_GET()

    def do_POST(self):
        if self.path != "/admin":
            return self._send(404, "Not found")
        n = int(self.headers.get("Content-Length", 0))
        d = parse_qs(self.rfile.read(n).decode())
        if d.get("user") == ["admin"] and d.get("pass") == ["admin123"]:
            return self._send(200, "Bienvenue admin. HACK{identifiants_par_defaut}")
        self._send(401, "Identifiants invalides")

    def log_message(self, *a):
        pass

class FTP(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.sendall(b"220 HACKademy-FTPd 1.0 (flag: HACK{banniere_bavarde}) ready\r\n")

if __name__ == "__main__":
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    ftp = socketserver.ThreadingTCPServer((HOST, 2121), FTP)
    threading.Thread(target=ftp.serve_forever, daemon=True).start()
    HTTPServer.allow_reuse_address = True
    print(f"[+] Cible active : http://{HOST}:8080  et  {HOST}:2121  (Ctrl+C pour arrêter)")
    HTTPServer((HOST, 8080), H).serve_forever()
