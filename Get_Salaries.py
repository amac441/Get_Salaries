
import mechanize
import urllib2  #maybe python3
import urllib
import time
import threading
import os
import re

##htmltext =  urllib.urlopen("http://www.fedsdatacenter.com/federal-pay-rates/output.php?n=&a=&l=&o=&y=&sEcho=20&iColumns=9&sColumns=&iDisplayStart=0&iDisplayLength=1000").read()

## reading the json response
## gives back an associative array (hashmap)  -  I need to give it a key

#i = 0

#while (i < 6000):
#    #3850768
#    start = str(i)
#    url = "http://www.fedsdatacenter.com/federal-pay-rates/output.php?n=&a=&l=&o=&y=&sEcho=20&iColumns=9&sColumns=&iDisplayStart=" + start + "&iDisplayLength=5000"
#    print url
#    htmltext =  urllib.urlopen(url)
#    data = json.load(htmltext)
#    jobs = data["aaData"]
#        for j = (0,5000):
            
#    file.write(str(jobs))
#    i = i + 5000

#jobs1 = jobs[1] #this gives you one row
#column2 = jobs1[3] #this gives you one column
#print jobs1
#print column2
#print data

#-------- tutorial on dealing with json -------
#http://similarsitesearch.com/api/similar/{url}
#htmltext = urllib.urlopen('http://similarsitesearch.com/api/similar/ebay.com').read()
#data = json.loads(htmltext)

#dat2 = [v for k, v in data.items() if type(v) == unicode and v != 'ok']

#people want to know what the fuck to study...
#kahn academy
#codeschool
#treehouse
#pluralsight
#cloudera
#udemy

