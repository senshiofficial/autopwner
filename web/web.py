import http.server
import socketserver

# Set the port number you want to use
port = 8000

# Specify the directory containing your HTML files
web_root = "http"

# Create a handler to serve the files
handler = http.server.SimpleHTTPRequestHandler

# Set up the server
with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Serving on port {port} from the {web_root} directory")

    # Change to the specified directory
    httpd.serve_forever()
