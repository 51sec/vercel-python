from http.server import BaseHTTPRequestHandler
from urllib import parse

class handler(BaseHTTPRequestHandler):

	def do_GET(self):
		s = self.path
		dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
		self.send_response(200)
		self.send_header('Content-type','text/plain')
		self.end_headers()

		
		
        ip_addr1 = request.remote_addr
        ip_addr2 = request.environ['REMOTE_ADDR']
        ip_addr3 = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
	
	
        return "</BR>" +"</BR>" +"</BR>" +"<h1>Welcome to My PY website!</h1>"+"</BR>" + "<h1> Your IP address is:" + ip_addr1 +"</BR>" + "<h1> Your IP address is:" + ip_addr2 + "</BR>" + "<h1> Your IP address is:" + ip_addr3

