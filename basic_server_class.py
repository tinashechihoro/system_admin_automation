class Server(object):
	"""A basic user of classes 
	for a server class
	"""
	def __init__(self,ip,hostname):
		"""initializing the server object"""
		self.ip = ip
		self.hostname

	def set_ip(self,ip):
		self.ip = ip

	def set_hostname(self,hostname):
		self.hostname = hostname

	def ping(self,ip_address):
		print('Ping {}  from  {} '.format(self.ip,self.hostname))

if '__name__' == '__main__':
	server = Server('120.0.0.1','localhost')
	server.ping('127.0.0.1')
