from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from config import PORT
from routes.chat import handle_chat
from routes.memory import handle_memory
from routes.health import handle_health
from security.auth import verify_api_key
from security.rate_limit import check_rate_limit

class EDITHServer(BaseHTTPRequestHandler):

    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_POST(self):
        if not verify_api_key(self.headers):
            self._set_headers(401)
            self.wfile.write(json.dumps({"error": "Unauthorized"}).encode())
            return

        if not check_rate_limit(self.client_address[0]):
            self._set_headers(429)
            self.wfile.write(json.dumps({"error": "Too many requests"}).encode())
            return

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)

        if self.path == "/chat":
            response = handle_chat(data)
        elif self.path == "/memory":
            response = handle_memory(data)
        else:
            response = {"error": "Invalid endpoint"}

        self._set_headers()
        self.wfile.write(json.dumps(response).encode())

    def do_GET(self):
        if self.path == "/health":
            self._set_headers()
            self.wfile.write(json.dumps(handle_health()).encode())

def run():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, EDITHServer)
    print(f"EDITH running on port {PORT}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

server = HTTPServer(("0.0.0.0", PORT), Handler)

if __name__ == "__main__":
    print(f"Starting server on port {PORT}")
    server.serve_forever()