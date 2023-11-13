import wsgiref.simple_server

def application(environ, start_response):
    content_type = "text/html"
    with open("example.html","r") as f:
        response = f.read().encode()
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

