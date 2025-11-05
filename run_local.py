import http.server
import socketserver
import webbrowser
import threading
import time

PORT = 8000

def open_browser():
    time.sleep(1)
    webbrowser.open(f"http://127.0.0.1:{PORT}")
    # Auto open your promo links
    promo_links = [
        "https://tntdesigns338.github.io/tntdesigns-site/",
        "https://www.amazon.com/shop/tntdesigns338",
        "https://www.instagram.com/tntdesigns338/",
        "https://www.tiktok.com/@tntdesigns338"
    ]
    for link in promo_links:
        webbrowser.open_new_tab(link)

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"🚀 Serving TnTDesigns site at http://127.0.0.1:{PORT}")
    threading.Thread(target=open_browser).start()
    httpd.serve_forever()
