import http.server
import socketserver
import webbrowser
import os

# Port for local server
PORT = 8000
url = f"http://127.0.0.1:{PORT}"

# Serve the folder this script is in
web_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(web_dir)

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Silence console logs if you want

print(f"\n🚀 Starting TnTDesigns local server at {url}\n")

# Open local site
webbrowser.open(url)

# 🔥 Auto-launch your promo sites
promo_links = [
    "https://tntdesigns338.github.io/tntdesigns-site/",
    "https://www.amazon.com/shop/tntdesigns338",
    "https://www.instagram.com/tntdesigns338/",
    "https://www.tiktok.com/@tntdesigns338"
]

for link in promo_links:
    try:
        webbrowser.open_new_tab(link)
    except Exception as e:
        print(f"Could not open {link}: {e}")

print("Opening promo links...")

# Run the local web server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Press CTRL+C to stop the server.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped. All promo tabs opened successfully.")
