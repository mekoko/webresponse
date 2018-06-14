#coding:utf-8  

from urllib2 import Request, urlopen, URLError, HTTPError  
import ssl
import socket
import httplib
ssl.match_hostname = lambda cert, hostname: True

def show_status(url):  
	headers = { 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' }  
	req = Request(url,'',headers)
	try:  
		response = urlopen(req,timeout=1)  
	except HTTPError, e:  
		return url,'Error code: ', e.code
	except URLError, e:  
		return url,'Reason: ', e.reason 
	except socket.timeout as e:  
		return url,type(e) 
	except ValueError,e:
		return url,'ValueError：',type(e)
	except ssl.SSLError,e:
		return url,'ssl.SSLError：',type(e)
	except socket.error,e:
		return url,'socket.error：',type(e)
	except httplib.BadStatusLine,e:
		return url,'httplib.BadStatusLine：',type(e)
	else:  
		return url,'Success'
  
def main():  
	f= open("urls.txt","r")
	res=open("res.txt","w")
	while 1:    
		lines = f.readlines()
		i=1
		for url in lines:
			code = show_status(url)
			print i,code
			res.write(code.__str__()+'\n')
			i=i+1
if __name__=="__main__":  
	main()  