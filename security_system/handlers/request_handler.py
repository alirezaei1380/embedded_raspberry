from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

import cgi
from security_system.models import Raspberry

hostName = "localhost"
hostPort = 8000

user_code = ''
admin_code = ''


class MyServer(BaseHTTPRequestHandler):

    def do_POST(self):
        global user_code, admin_code
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        nuser_code = form.getvalue('user_code')
        nadmin_code = form.getvalue('admin_code')
        if not nadmin_code or not nuser_code:
            return
        Raspberry.objects.create(admin_code=nadmin_code, user_code=nuser_code)
        user_code = nuser_code
        admin_code = nadmin_code
        self.send_response(200)


def get_passwords():
    global user_code, admin_code
    return user_code, admin_code


myServer = HTTPServer((hostName, hostPort), MyServer)


def run_server():
    myServer.serve_forever()
