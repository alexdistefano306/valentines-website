from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = "0.0.0.0"
PORT = 8000


def main() -> None:
    server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
    print(f"Serving Valentine's page at http://{HOST}:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    main()
