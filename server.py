import http.server
import socketserver
import os

replica = os.environ.get('CS_REPLICA')
server = os.environ.get('SERVER_NAME')
port = int(os.environ.get('PORT'))

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(
            f'\tResponse:{server}:{replica}:{self.path}\n.encode('utf-8')
        )

with socketserver.TCPServer(('', port), RequestHandler) as httpd:
    print(f'Serving at port: {port}')
    httpd.serve_forever()