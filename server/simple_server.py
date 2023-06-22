import http.server
import socketserver
import psycopg2
import json


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Connect to PostgreSQL
        connection = psycopg2.connect(
            host="db",
            port=5432,
            dbname="sreality",
            user="sreality_user",
            password="sreality_pass"
        )

        # Query 500 items from the database
        cursor = connection.cursor()
        cursor.execute("SELECT title, image_url FROM items LIMIT 500;")
        rows = cursor.fetchall()

        # Create an HTML response
        html_content = """<html>
                            <head>
                                <title>Items</title>
                                <meta charset="UTF-8">
                            </head>
                            <body>"""
        for row in rows:
            title, image_urls = row
            html_content += f"<h2>{title}</h2>"
            # Assuming image_urls is stored as list of strings in the database
            for image_url in image_urls:
                html_content += f"<img src=\"{image_url}\" />"
        html_content += "</body></html>"

        # Send the HTML response
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html_content.encode("utf-8"))


# Run the HTTP server on port 8080
PORT = 8080
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"serving at port {PORT}")
    httpd.serve_forever()
