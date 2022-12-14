#!/usr/bin/env python3

from socket import gethostname
from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus
from time import time
import sys

unhealthy = False
start_time = time()


class RequestHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        global unhealthy
        global start_time
        if self.path == "/health" or self.path == "/live":
            if unhealthy is True:
                self.send_error(HTTPStatus.INTERNAL_SERVER_ERROR)
            else:
                self.send_response(200)
                self.end_headers()
        elif self.path == "/ready":
            if time() - start_time < 10:
                self.send_error(HTTPStatus.SERVICE_UNAVAILABLE)
            else:
                self.send_response(200)
                self.end_headers()
        elif self.path == "/get-sick":
            unhealthy = True
            self.send_response(200)
            self.end_headers()
        elif self.path == "/get-well":
            unhealthy = False
            self.send_response(200)
            self.end_headers()
        elif self.path == "/die":
            self.log_message("Time to die")
            self.send_response(200)
            self.end_headers()
            self.flush_headers()
            sys.exit(0)
        elif self.path == "/":
            self.send_response(200)
            msg = f"hello from {gethostname()}\n"
            content = msg.encode(encoding="utf-8", errors="replace")
            self.send_header("Content-Type", "text/plain;charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        else:
            self.send_error(HTTPStatus.NOT_FOUND)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, HEAD, OPTIONS")
        self.end_headers()

    def do_POST(self):
        self.send_error(HTTPStatus.NOT_IMPLEMENTED)

    def send_error(self, code, message=None, explain=None):
        if code in (HTTPStatus.METHOD_NOT_ALLOWED, HTTPStatus.NOT_IMPLEMENTED):
            code = HTTPStatus.METHOD_NOT_ALLOWED
            self.send_response(code, code.phrase)
            self.send_header("Allow", "GET, HEAD, OPTIONS")
            self.send_header("Connection", "close")
            self.end_headers()
        else:
            super().send_error(code, code.phrase, code.description)
        return


def main():
    port = 5000
    server = HTTPServer(("", port), RequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
