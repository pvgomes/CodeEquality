from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1> Hello, Poznannnn! </h1> ')

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHandler)
    print('Starting server on port 8000...')
    httpd.serve_forever()
