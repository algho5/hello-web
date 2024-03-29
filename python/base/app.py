import BaseHTTPServer
import json

class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
  def do_GET(self):

    if self.path == "/":
      self.send_response(200)
      self.send_header("content-type", "application/json")
      self.end_headers()
      self.wfile.write(json.dumps({"message": "Hello, World!"}))
      return

    self.send_response(404)
    self.send_header("content-type", "application/json")
    self.end_headers()
    self.wfile.write(json.dumps({"error": "Not found"}))

if __name__ == '__main__':
  address = ('', 8080)
  server = BaseHTTPServer.HTTPServer(address, Handler)
  server.serve_forever()
