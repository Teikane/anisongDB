from http.server import HTTPServer, SimpleHTTPRequestHandler, test as site_og
import sys

def site (*args):
	site_og (*args, port=int(sys.arg[1]) if len(sys.argv) > 1 else 7500)

class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
	site(CORSRequestHandler, HTTPServer)
	print ("HELLO WORLD!")