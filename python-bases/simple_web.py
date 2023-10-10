import wsgiref.simple_server

def application(environ, start_response):
    content_type = "text/html"
    response = b'<h1 style="color:red">Hello</h1>'
    status = "200 OK"

    headers = [
        ("Content-Type",content_type),
        ("Content-Length",str(len(response)))
    ]

    start_response(status, headers)
    return [response]
    

if __name__ == "__main__":
    print("Running web server...")
    w_s = wsgiref.simple_server.make_server(
        host="localhost",
        port=8021,
        app=application
    )
    w_s.serve_forever()