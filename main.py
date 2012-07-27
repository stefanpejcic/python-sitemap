import re
from urllib.request import urlopen, Request
from urllib.parse import urlparse

import argparse

# Gestion des parametres
parser = argparse.ArgumentParser(version="0.1",description='Crawler pour la creation de site map')
parser.add_argument('--domain', action="store", default="",required=True, help="Target domain (ex: http://blog.lesite.us)")
parser.add_argument('--debug', action="store_true", default=False, help="Enable debug mode")
parser.add_argument('--output', action="store", default=None, help="Output file")

arg = parser.parse_args()

outputFile = None
if arg.output is not None:
	try:
		outputFile = open(arg.output, 'w')
	except:
		if not arg.debug:
			print ("Output file not available.")
			exit(255)
		else:
			print ("Continue without output file.")


tocrawl = set([arg.domain])
crawled = set([])
linkregex = re.compile(b'<a href=[\'|"](.*?)[\'"].*?>')

header = """
<?xml version="1.0" encoding="UTF-8"?>
<urlset
      xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
            http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
<!-- created with Free Online Sitemap Generator www.xml-sitemaps.com -->

"""
footer = "</urlset>"

try:
	target_domain = urlparse(arg.domain)[1]
except:
	print ("Invalid domain")

print (header, file=outputFile)
while tocrawl:
	crawling = tocrawl.pop()

	url = urlparse(crawling)
	try:
		request = Request(crawling, headers={"User-Agent":'Sitemap crawler'})
		response = urlopen(request)
		msg = response.read()
		response.close()
	except Exception as e:
		if arg.debug:
			print ("{1} ==> {0}".format(e, crawling))
		continue

	
	links = linkregex.findall(msg)
	# print (links)
	# for link in links:
	# 	print (link)
	crawled.add(crawling)
	#for link in (links.pop(0) for _ in range(len(links))):
	for link in links:
		link = link.decode("utf-8")
		if link.startswith('/'):
			link = 'http://' + url[1] + link
		elif link.startswith('#'):
			link = 'http://' + url[1] + url[2] + link
		elif not link.startswith('http'):
			link = 'http://' + url[1] + '/' + link
		
		# Remove the anchor part if needed
		if "#" in link:
			link = link[:link.index('#')]

		domain_link = urlparse(link)[1]
		if (link not in crawled) and (link not in tocrawl) and (domain_link == target_domain) and ("javascript:" not in link):
			#content += "<url><loc>"+link+"</loc></url>"
			print ("<url><loc>"+link+"</loc></url>", file=outputFile)
			tocrawl.add(link)
print (footer, file=outputFile)

#print len(crawled)