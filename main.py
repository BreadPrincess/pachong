# coding:utf-8

import urllib2
import re

import sys 
from domysql import *


reload(sys) 
sys.setdefaultencoding('utf8')


baseurl = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2014/index.html'


strHtml = urllib2.urlopen(urllib2.Request(baseurl)).read().decode('gb2312')
#print strHtml




regbase = '<a href=\'(\d*)\.html\'>'
item =  re.findall(regbase,strHtml)
#print item
preurl = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2014/'

k = 1



for xx in item:
#	print preurl+ xx

	strHtml1 = urllib2.urlopen(urllib2.Request(preurl+ xx +'.html')).read().decode('gb2312')

	reg1 = r'<a href=\'(\d*/\d*)\.html\'>'
	item1 =  re.findall(reg1,strHtml1)
	for xxx in item1:
#		print preurl+ xxx + '.html'
		
		try:
	

			strHtml2 = urllib2.urlopen(urllib2.Request(preurl+ xxx+'.html')).read().decode('gb2312')

			reg2 = r'<a href=\'(\d*/\d*)\.html\'>'
			reg21 = r'<a href=\'(\d*/)\d*\.html\'>'
			item2 =  re.findall(reg2,strHtml2)
			item21 =  re.findall(reg21,strHtml2)
			for xxxx in range(len(item2)):
#				print preurl+ xx +'/'+ item2[xxxx]+ '.html'
				try:
					strHtml3 = urllib2.urlopen(urllib2.Request(preurl+ xx +'/'+ item2[xxxx]+ '.html')).read().decode('gb2312')

					reg3 = r'<a href=\'(\d*/\d*)\.html\'>'
					item3 =  re.findall(reg3,strHtml3)
					for x5 in item3:
#						print preurl+ xx+'/'+item21[xxxx]  + x5 +'.html'
						
						strHtml6 = urllib2.urlopen(urllib2.Request( preurl+ xx+'/'+item21[xxxx]  + x5 +'.html')).read().decode('gb2312')

						reg6 = r'><td>(\d*)</td>'
						reg61 = r'<td>(\W*)</td>'
						item6 =  re.findall(reg6,strHtml6)
						item61 = re.findall(reg61,strHtml6)
						for x6 in range(len(item6)):
							print "%s %s" %(item6[x6],item61[x6])



#							cmd = 'insert into cun values(%d,%d,\'%s\');'%(0,int(item6[x6]),item61[x6])
#							do_mysql_cmd(cmd)

				except:
					print "notfound3"

				
					


		except:
			print 'not found'
			pass
			









sss = '''









kk = 1










for xx in item:

	strHtml = urllib2.urlopen(urllib2.Request(preurl+xx)).read().decode('gb2312')
	


	
	
	



	reg = r'>(\d*)</a></td><td><a href'
	reg1 = r'>(\W*)</a></td></tr>'
	item =  re.findall(reg,strHtml)
	item1 = re.findall(reg1,strHtml)

	for x in range(len(item)):
		print "%s  %s"%(item[x],item1[x])

		
		kk+=1
print kk



'''


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
