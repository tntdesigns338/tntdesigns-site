import http.server
import socketserver
import webbrowser

PORT = 8000
url = f"http://127.0.0.1:{PORT}"

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # optional: silence console logs

print(f"\n🚀 Starting TnTDesigns local server at {url}\n")
webbrowser.open(url)  # auto-open in default browser

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Press CTRL+C to stop the server.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
