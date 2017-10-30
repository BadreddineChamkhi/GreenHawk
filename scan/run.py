#!usr/bin/python
# -*- coding: utf-8 -*-
#C0ded By Badreddine Chamkhi
#Don't Change my Copyright
#Shareout To Fallga Team Tunisian Cyber Resistance
#IpScanner | Get All Websites => Wodpress => Joomla => OpenCart => .....
#Sun 22:33
#import zone
import os
import sys
from platform import system
import urllib2
import time
import re
import urllib
import httplib
import os
import cookielib
import requests as xsec
from time import sleep
from threading import Thread
import socket
from ftplib import FTP
#~~~~~~~~~~~~~~~~~~~~~
users = []#SimpleUsers
susers = []#SuperUsers
sites = []#Sites
grabbed = []#GrabbedSites
wplist = [] #WodpressList
jolist = []#JoomlaList
oclist = []#OpenCartList
sqlilist = []#SqlList
#~~~~~~~~~~~~~~~~~~~~~
style = '''
<style>
body,table{background: black; font-family:Verdana,tahoma; color: white; font-size:14px; }
A:link {text-decoration: none;color: red;}
A:active {text-decoration: none;color: red;}
A:visited {text-decoration: none;color: red;}
A:hover {text-decoration: underline; color: red;}
#new,input,table,td,tr,#gg{border-style:solid;text-decoration:bold;}
input:hover,tr:hover,td:hover{background-color: #FFFFCC; color:green;}
</style>
'''
#~~~~~~~~~~~~~~~~~~~~~Banner masrou9 xd~~~~~~~~~~~~~~~~~~~~~

def clear():
	if system() == 'Linux':
		os.system('clear')
	if system() == 'Windows':
		os.system('cls')
clear()
#~~~~~~~~~~~~~~~~~~~~~
def banner(): 
 print ''' \033[1;32m
     ▄▀  █▄▄▄▄ ▄███▄   ▄███▄      ▄    ▄  █ ██     ▄ ▄   █  █▀ 
   ▄▀    █  ▄▀ █▀   ▀  █▀   ▀      █  █   █ █ █   █   █  █▄█   
   █ ▀▄  █▀▀▌  ██▄▄    ██▄▄    ██   █ ██▀▀█ █▄▄█ █ ▄   █ █▀▄   
   █   █ █  █  █▄   ▄▀ █▄   ▄▀ █ █  █ █   █ █  █ █  █  █ █  █  
    ███    █   ▀███▀   ▀███▀   █  █ █    █     █  █ █ █    █   
          ▀                    █   ██   ▀     █    ▀ ▀    ▀    
                                              ▀                 
\033[1;m 
'''
banner()
#~~~~~~~~~~~~~~~~~~~~~
def author():
 print ''' \033[1;38m
			C0ded By Badreddine Chamkhi
\033[1;m
'''
author()
#~~~~~~~~~~~~~~~~~~~~~
print ''' 
	      \033[1;42m[ GreenHawk v 1.0 ]\033[1;m
              \033[1;42m[ AutoCmsScanner & Website Grabber  ]\033[1;m			
'''
#~~~~~~~~~~~~~~~~~~~~~
def extrctsrv(ip):
	try :
		page= 1 
		while page <= 21:
			bing = "http://www.bing.com/search?q=ip%3A"+ip+"+&count=50&first="+str(page)
			openbing = urllib2.urlopen(bing)
			readbing = openbing.read()
			findwebs = re.findall('<h2><a href="(.*?)"' , readbing)
			for i in sitess :
				sites.append(i)
			print " | Grabbed "+str(len(sites))+ " Sites |"
			page = page + 21
	except :
	  pass
#~~~~~~~~~~~~~~~~~~~~~
def extrctusers():
	try:
		for site in sites :
			site = site.replace("http://","")
			site1= site.replace("/","")
		try:
			site2,dash = site1.split(".")
		except:
			site2 = "none"
		i = 0
		while i <= len(site2):
			cuser= site2[i:0]
			users.append(cuser)	
	except:
	  pass
#~~~~~~~~~~~~~~~~~~~~~
def getwpsite(ip):
	print "\033[1;44m| Grabbing Wordpress ...\033[1;m "
	try:
		page = 1 
		while page <= 101:
			bing = "http://www.bing.com/search?q=ip%3A" +ip+ "+?page_id=&count=50&first=" + str(page)
			openbing = urllib2.urlopen(bing)
			readbing = openbing.read()
			findwebs = re.findall('<h2><a href="(.*?)"' , readbing)
			for i in range(len(findwebs)):
				wp= findwebs[i]
				findwp= re.findall('(.*?)\?page_id=' , wp)
				wplist.extend(findwp)
			page = page + 10
       		print "\033[1;44m|- Grabbed : " + str(len(wplist)) + " Wordpress Sites \033[1;m"
	except:
	  pass
#~~~~~~~~~~~~~~~~~~~~
def getjosite(ip):
	print "\033[1;42m| Grabbing Joomla ...\033[1;m"
	try:
		page = 1 
		while page <= 21 :
			bing = "http://www.bing.com/search?q=ip%3A"+ip+"+index.php?option=com&count=50&first="+str(page)
			openbing= urllib2.urlopen(bing)
			readbing = openbing.read()
			findwebs= re.findall('<h2><a href="(.*?)"' , readbing)
			for i in range(len(findwebs)):
				js= findwebs[i]
				findjs= re.findall('(.*?)index.php', js)
				jolist.extend(findwebs)
			page = page + 10
		print "\033[1;42m|- Grabbed : " + str(len(jolist)) + " Joomla Sites |\033[1;m"
	except:
	  pass
#~~~~~~~~~~~~~~~~~~~~~~
def getopencart(ip):
	print "\033[1;43m| Grabbing OpenCart ...\033[1;m"
	try:
		page = 1
		while page <=21:
			bing = "http://www.bing.com/search?q=ip%3A"+ip+"+admin&count=50&first="+str(page)
			openbing= urllib2.urlopen(bing)	
			readbing = openbing.read()	
			findwebs = re.findall('<h2><a href="(.*?)"' , readbing)
			for i in range(len(findwebs)):
				oc= findwebs[i]
				findoc=re.findall('>OpenCart<',oc)
				oclist.extend(findwebs)
			page = page + 10
		print "\033[1;43m|- Grabbed "+str(len(oclist))+ " OpenCart Sites |\033[1;m"
	except:
	  pass
#~~~~~~~~~~~~~~~~~~~~~~~~
def grabsqli(ip):
    try :
        print "\033[1;45m| Grabbing Sqli ... \033[1;m"
        page = 1
        while page <= 21:
                bing = "http://www.bing.com/search?q=ip%3A"+ip+"+.php?id=&count=50&first="+str(page)
                openbing  = urllib2.urlopen(bing)
                readbing = openbing.read()
                findwebs = re.findall('<h2><a href="(.*?)"' , readbing)
                sites = findwebs
                for i in sites :
                            try :
                                      response = urllib2.urlopen(i).read()									 
                                      checksqli(i)	
                            except urllib2.HTTPError, e:
                                       str(sites).strip(i)
								   
                page = page + 10 
	print "\033[1;45m|- Grabbed Sqli " + str(len(sqlist)) + " Sqli Sites\033[1;m|"
    except : 
         pass
#~~~~~~~~~~~~~~~~~~~~~~~~~
def checksqli(sqli):
                            responsetwo = urllib2.urlopen(sqli + "'").read()
                            find = re.findall("sql",responsetwo)
                            if find:
                                            sqlilist.append(sqli)   
#~~~~~~~~~~~~~~~~~~~~~~~~
def scanwp():
	try:
            print bcolors.OKBLUE + "| Scanning Wordpress From most Known plugins"
            for wp in wplist :
                    for link,name in wpt.iteritems() :
                                currentcodetwo = urllib.urlopen(wp + "/" + str(link)).getcode()
                                if currentcodetwo == 200 :
                                            print "|-> Found Wordpress Plugin " +  str(name) + " In "  + str(wp)
	except:
	  pass	
#~~~~~~~~~~~~~~~~~~~~~~~~
def scanjoomla():
     try :
            print bcolors.OKBLUE + "|- Scanning Joomla From most Known Components"
            for jo in jolist :
                    for link,name in jot.iteritems() :
                                currentcodetwo = urllib.urlopen(jo + "/" + str(link)).getcode()
                                if currentcodetwo == 200 :
                                            jocheck = urllib2.urlopen(jo + "/" + str(link)).read()
                                            found = re.findall(str(name), jocheck)
                                            if found :
                                                    print  "|-> Found Joomla " + str(name) + " In " +  + str(jo)
     except :
         pass
#~~~~~~~~~~~THose Codes From Showwp Are Not My Codes i just updated the code ;) Shareout TO the real owner :)~
def showwp(ip):
    with open("Rep/" + ip + '_rep.html', 'a') as f:
         f.write('<center><font color="yellow" size=4>WORDPRESS </font><font color="blue" size=4>SITES</font><font color="green" size=4></font></center>' )
         f.write('<center><textarea rows="10" cols="40">' )
         f.close()
    for wp in wplist :
	         with open("Rep/" + ip + '_rep.html', 'a') as f:
                   f.write(wp  + "\n")
    f.close()		 
    with open("Rep/" + ip + '_rep.html', 'a') as f:
         f.write('</textarea>' )
         f.close()
def showjo(ip):
    with open("Rep/" + ip + '_rep.html', 'a') as f:
         f.write('<center><font color="yellow" size=4>Joomla  </font><font color="blue" size=4>SITES</font><font color="green" size=4></font></center>' )
         f.write('<center><textarea rows="10" cols="40">' )
         f.close()
    for jo in jolist :
	         with open("Rep/" + ip + '_rep.html', 'a') as f:
                   f.write(jo  + "\n")
    f.close()		 
    with open("Rep/" + ip + '_rep.html', 'a') as f:
         f.write('</textarea>' )
         f.close()
def showsqli(ip):
    with open("Rep/" + ip + '_rep.html ','a') as f:
         f.write('<center><font color="yellow" size=4>SQL Injection   </font><font color="blue" size=4>SITES</font><font color="green" size=4></font></center>' )
         f.close()
    for sq in sqlilist :
	         with open("Rep/" + ip + '_rep.html', 'a') as f:
                   f.write('<br><a href="' + str(sq) + '"><font color="blue" size="3">' + str(sq) + '</font></a><br>')
    f.close()	
def showoc(ip):
	with open("Rep/" + ip + '_rep.html ','a') as f:
		 f.write('<center><font color="yellow" size=4>OpenCart   </font><font color="blue" size=4>SITES</font><font color="green" size=4></font></center>' )
		 f.close()
	for oc in oclist :
		with open("Rep/" + ip + '_rep.html', 'a') as f:
			f.write('<br><a href="' + str(oc) + '"><font color="blue" size="3">' + str(oc) + '</font></a><br>')
	f.close()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~
ips = open('ip.txt','r')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main(ip):
    del jolist[:]
    del wplist[:]
    del sqlilist[:]
    del sites[:]
    try :
        ip = socket.gethostbyname(ip)
    except :
        pass
    with open("Rep/" + ip + '_rep.html', 'a') as f:
        f.write("<html>")
        f.write(style)
        f.write('<hr color="red">')
    print "\033[1;41m|-> Target :" + str(ip) + " Working... \033[1;m "
    extrctsrv(ip)
    getwpsite(ip)
    showwp(ip)
    getjosite(ip)
    showjo(ip)
    getopencart(ip)
    showoc(ip)
    grabsqli(ip)
    showsqli(ip)
for ip in ips :
    ip = ip.rstrip()
    main(ip)
print "\033[1;41m[+] Job Completed ! You Will Find Your Result In Rep File :)\033[1;m"
#Done In Mon 14:09 :) Coded By Badreddine CHamkhi DOn't Change it :) 
#Contact : Email -> bchemkh.1919@gmail.com | Facebook -> www.facebook.com | GitHub -> www.github.com/BadreddineCHamkhi
#My Copyright So Don't Change it :)
		 

				
