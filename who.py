import whois
import time


def who(url):
	url = url.strip()
	try:
		w = whois.whois(url)
		print url
		print w.emails
		f = open('emails.txt','a');
		f.write(url+','+ w.name+','+str(w.emails)+'\r\n')
	except Exception, e:
		print "e"
	time.sleep(1)



with open("domains.txt", "r") as f:
    for line in f:
        who(line)
