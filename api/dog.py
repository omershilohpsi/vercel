from http.server import BaseHTTPRequestHandler
from datetime import datetime
from random import randint

with open('../pictures/dog.txt') as pictures:
pics = pictures.read().splitlines()

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    self.wfile.write('<img src="' + pics[randint(0, len(pics) - 1)] + '"/>'.encode())
    return
