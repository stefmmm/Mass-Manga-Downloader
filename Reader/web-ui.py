from http.server import BaseHTTPRequestHandler, HTTPServer
import os
hostName = "localhost"
serverPort = 8080


dir = os.listdir('../Library/Pururin')


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head></head>", "utf-8"))
        self.wfile.write(bytes("<title>MMD Reader</title>", "utf-8"))
        self.wfile.write(bytes("<link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/uikit@3.11.1/dist/css/uikit.min.css'/>", "utf-8"))
        self.wfile.write(bytes("<script src='https://cdn.jsdelivr.net/npm/uikit@3.11.1/dist/js/uikit.min.js'></script>", "utf-8"))
        self.wfile.write(bytes("<script src='https://cdn.jsdelivr.net/npm/uikit@3.11.1/dist/js/uikit-icons.min.js'></script>", "utf-8"))
        self.wfile.write(bytes("</head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<div class='uk-section-secondary'>", "utf-8"))
        self.wfile.write(bytes("<div class='uk-container-expand'>", "utf-8"))
        self.wfile.write(bytes("<div class='uk-card uk-card-body uk-card-secondary'>", "utf-8"))
        self.wfile.write(bytes("<h3 class='uk-card-title uk-text-center'>MMD Reader</h3>", "utf-8"))
        self.wfile.write(bytes("<table class='uk-table uk-table-middle uk-table-divider'>", "utf-8"))
        self.wfile.write(bytes("<thead><tr><th class='uk-width-small'>Module</th><th>Manga Name</th></tr>", "utf-8"))
        self.wfile.write(bytes("<tbody>", "utf-8"))

        for files in dir:


            self.wfile.write(bytes(f"<tr><td>Pururin</td><td>{str(files)}</td><td><a class='uk-button uk-button-default uk-align-right' href='http://localhost:8081/?manga={str(files)}'>Read</a></td></tr>", "utf-8"))
        self.wfile.write(bytes("</tbody>", "utf-8"))
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