import json
import wsgiref.simple_server
import urllib.parse

forms_data = []  # all submissions

def application(environ, start_response):
    # requested path
    path = environ["PATH_INFO"]
    # requested method
    method = environ["REQUEST_METHOD"]
    
    # content type of response
    content_type = "text/html"

    if path == "/":
        if method == "POST":
            # getting wsgi.input obj
            input_obj = environ["wsgi.input"]
            # length of body
            input_length = int(environ["CONTENT_LENGTH"])
            # getting body of wsgi.input obj
            # decoding to string
            body = input_obj.read(input_length).decode()

            # parsing body of form
            data = urllib.parse.parse_qs(body, keep_blank_values=True)
            # data of body in format
            name = data["name"][0]
            age = int(data["age"][0])
            
            if (age >= 18):
                response_message = "" + name + " You're in the list that can drink alcahol."
            else:
                response_message = "" + name + "You're in the list that can't drink alcahol."
            
            response = bytes(response_message, 'utf-8')
            status = "200 OK"
        else:
            # reading html file
            with open("drink_form.html","r") as f:
                response = f.read().encode()
            status = "200 OK"

    elif path == "/forms":
        # if /forms path
        # converting to JSON data
        response = json.dumps(forms_data).encode()
        status = "200 OK"
        # changing content-type
        content_type = "application/json"

    else:
        # 404 - path not found
        response = b"<h1>Not found</h1><p>Entered path not found</p>"
        status = "404 Not Found"

    # response headers
    headers = [
        ("Content-Type",content_type),
        ("Content-Length",str(len(response)))
    ]

    start_response(status, headers)
    return [response]
    

if __name__ == "__main__":
    w_s = wsgiref.simple_server.make_server(
        host="localhost",
        port=8021,
        app=application
    )
    w_s.serve_forever()