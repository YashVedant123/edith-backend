from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from routes.chat import handle_chat
import os
from config import PORT

API_SECRET = os.getenv("API_SECRET", "edith-secret")

class Handler(BaseHTTPRequestHandler):

    def do_POST(self):
        if self.path != "/chat":
            self.send_response(404)
            self.end_headers()
            return

        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)

        try:
            data = json.loads(body)

            # API key validation
            api_key = self.headers.get("X-API-KEY")
            if api_key != API_SECRET:
                self.send_response(403)
                self.end_headers()
                self.wfile.write(b'{"response": "Unauthorized"}')
                return

            response = handle_chat(data)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(
                json.dumps({"response": f"Server error: {str(e)}"}).encode()
            )

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Server running on port {PORT}")
    server.serve_forever()
