 self.end_headers()
    self.wfile.write(b'SPECIAL ONE...............NAAG!')
    return

  
def run():
  print('Server is starting...')
