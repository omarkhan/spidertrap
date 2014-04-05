#!/usr/bin/env python

try:
    from http.server import HTTPServer, BaseHTTPRequestHandler
except ImportError:
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler


response_template = """<!doctype html>
<html>
<body>
<ul>
{links}
</ul>
</body>
</html>
"""

link_template = '<li><a href="{base}{i}/">{base}{i}</a></li>'


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        links = [link_template.format(base=self.path, i=i)
                 for i in range(1, self.server.fanout + 1)]
        response = response_template.format(links='\n'.join(links))
        self.send_response(200)
        self.end_headers()
        self.wfile.write(response.encode('ascii'))


class Server(HTTPServer):
    def __init__(self, *args, **kwargs):
        self.fanout = kwargs.pop('fanout', 2)
        HTTPServer.__init__(self, *args, **kwargs)


if __name__ == '__main__':
    import argparse
    import sys
    parser = argparse.ArgumentParser(description='Spider trap for testing crawlers.')
    parser.add_argument('-p', '--port', type=int, default=9999, help='[9999]')
    parser.add_argument('--fanout', type=int, default=2,
                        help='Number of links to create on each page [2]')
    args = parser.parse_args()
    sys.stderr.write('Point your spider at localhost:{port}\n'.format(port=args.port))
    httpd = Server(('', args.port), Handler, fanout=args.fanout)
    httpd.serve_forever()
