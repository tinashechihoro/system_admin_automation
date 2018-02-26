#!/usr/bin/evn python3
# A apache config file parser

from cStringIO import StringIO
import re

vhost_start = re.compile(r'<VirtualHost\s+(.*?)?')
vhost_end = re.compile(r'</VirtualHost')
docroot_re = re.compile(r'(DocumentRoot\s+)(\S+)')

def replace_docroot(conf_string,vhost,new_docroot):
	'''
	yield new lines of an http.config file where docroot lines matching
	the specific vhost are repalced with new_docroot
	'''

	conf_file = StringIO(conf_string)
	in_vhost = False
	curr_vhost = None
	for line in conf_file:
		vhost_start_match = vhost_start.search(line)
		if vhost_start_match:
			curr_vhost = vhost_start_match.groups()[0]
			in_vhost = True
		if  in_vhost and (curr_vhost == vhost):
			docroot_match = docroot_re.search(line)
			if docroot_match:
				sub_line = docroot_re.sub(r'\1{0}s'.format(new_docroot,line
					line = sub_line
			vhost_end_match = vhost_end.search(line)
			if vhost_end_match:
				in_vhost = False
			yield line
if '__name__' == '__main__':
	import sys
	conf_file  = sys.argv[1]
	vhost = sys.argv[2]
	docroot = sys.argv[3]
	conf_string = open(conf_file).read()
	for line in replace_docroot(conf_string,vhost,docroot)
	print(line)


