from http.server import HTTPServer, BaseHTTPRequestHandler
import time
# Declare host and port
host = "192.168.56.1"
port = 9999


class HTTP_Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body>Hello world</body></html>", "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time": "' + date + '"}', "utf-8"))


server = HTTPServer((host, port), HTTP_Server)
print("Server now running.....")
server.serve_forever()

server.server_close()
print("Server stopped!")