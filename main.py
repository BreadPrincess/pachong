# coding:utf-8

import urllib2
import re

import sys 
reload(sys) 
sys.setdefaultencoding('utf8')


baseurl = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2014/index.html'


strHtml = urllib2.urlopen(urllib2.Request(baseurl)).read().decode('gb2312')
print strHtml


reg = '<a href=\'(\d*\.html)\'>'
item =  re.findall(reg,strHtml)
print item
preurl = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2014/'

for x in item:
#	print preurl+x

	strHtml = urllib2.urlopen(urllib2.Request(preurl+x)).read().decode('gb2312')

	reg = r'>(\d*)</a></td><td><a href'
	reg1 = r'>(\W*)</a></td></tr>'
	item =  re.findall(reg,strHtml)
	item1 = re.findall(reg1,strHtml)

	for x in range(len(item)):
		print "%s  %s"%(item[x],item1[x])






'''

url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2014/14.html'

strHtml = urllib2.urlopen(urllib2.Request(url)).read().decode('gb2312')

reg = r'>(\d*)</a></td><td><a href'
reg1 = r'>(\W*)</a></td></tr>'
item =  re.findall(reg,strHtml)
item1 = re.findall(reg1,strHtml)

for x in range(len(item)):
	print "%s  %s"%(item[x],item1[x])
'''
