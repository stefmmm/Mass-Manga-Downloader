from http.server import BaseHTTPRequestHandler, HTTPServer
from zipfile import ZipFile
import base64
from urllib.parse import urlparse
from urllib.parse import parse_qs

hostName = "localhost"
serverPort = 8081




class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):

        query_components = parse_qs(urlparse(self.path).query)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head></head>", "utf-8"))
        self.wfile.write(bytes("<title>MMA Reader</title>", "utf-8"))
        self.wfile.write(bytes("<link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/uikit@3.11.1/dist/css/uikit.min.css'/>", "utf-8"))
        self.wfile.write(bytes("<script src='https://cdn.jsdelivr.net/npm/uikit@3.11.1/dist/js/uikit.min.js'></script>", "utf-8"))
        self.wfile.write(bytes("<script src='https://cdn.jsdelivr.net/npm/uikit@3.11.1/dist/js/uikit-icons.min.js'></script>", "utf-8"))
        self.wfile.write(bytes("</head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<div class='uk-section-secondary'>", "utf-8"))
        self.wfile.write(bytes("<div class='uk-container'>", "utf-8"))
        self.wfile.write(bytes("<div class='uk-card uk-card-body uk-card-secondary'>", "utf-8"))
        self.wfile.write(bytes("<h3 class='uk-card-title uk-text-center'>MMD Reader</h3>", "utf-8"))

        if 'manga' in query_components:
            name = query_components["manga"][0]
            file_name = f"../Library/Pururin/{name}"
            with ZipFile(file_name, 'r') as zip:
                for file in zip.namelist():
                    print(file)
                    img = zip.open(file)
                    encoded = base64.b64encode(img.read())
                    self.wfile.write(bytes(f"<img class='uk-align-center' src=data:image/jpeg;base64,{encoded.decode('utf-8')} >", "utf-8"))

        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")