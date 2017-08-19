#import urllib2,re
#url = 'http://kaijiang.500.com/shtml/ssq/17023.shtml'
#res = urllib2.urlopen(url)
#page = res.read()
#pattern = re.compile('<div class="ball_box01">.*?<li class="ball_red">(.*?)</li>.*?<li class="ball_red">(.*?)</li>.*?<li class="ball_red">(.*?)</li>.*?<li class="ball_red">(.*?)</li>.*?<li class="ball_red">(.*?)</li>.*?<li class="ball_red">(.*?)</li>.*?<li class="ball_blue">(.*?)</li>.*?</div>',re.S)
#result = re.findall(pattern,page)
#print result[0][0],result[0][1],result[0][2],result[0][3],result[0][4],result[0][5],result[0][6]
#
__author__ = 'ikinest'
# -*- coding:utf-8 -*-
 
import urllib
import urllib2
import re
 
class Spider(object):
	def __init__(self,issueNo):
		self.url = 'http://kaijiang.500.com/shtml/ssq/'
		self.issueNo = issueNo
	def getPage(self):
		url = self.url+str(self.issueNo)+".shtml"
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		return response.read()
	def getHit(self,page):
		pattern = re.compile('<div class="ball_box01">.*?<li class="ball_red">(.*?)</li>.*?<li class="ball_red">(.*?)</li>.*?<li class="ball_red">(.*?)</li>.*?<li class="ball_red">(.*?)</li>.*?<li class="ball_red">(.*?)</li>.*?<li class="ball_red">(.*?)</li>.*?<li class="ball_blue">(.*?)</li>.*?</div>',re.S)
		result = re.findall(pattern,page)
		return result
	def createSqlOrTxt(self,result,flag):
		ball_red1 = str(result[0][0])
		ball_red2 = str(result[0][1])
		ball_red3 = str(result[0][2])
		ball_red4 = str(result[0][3])
		ball_red5 = str(result[0][4])
		ball_red6 = str(result[0][5])
		ball_blue = str(result[0][6])
		
		if flag == 'sql':
			return "INSTERT INTO Lottery_SSQ(issueNo,ball_red1,ball_red2,ball_red3,ball_red4,ball_red5,ball_red6,ball_blue)VALUES("+self.issueNo+","+ball_red1+","+ball_red2+","+ball_red3+","+ball_red4+","+ball_red5+","+ball_red6+","+ball_blue+")"+"\n"
		if flag == 'txt':
			return self.issueNo+","+str(ball_red1)+","+str(rball_red2)+","+str(ball_red3)+","+str(ball_red4)+","+str(ball_red5)+","+str(ball_red6)+","+str(ball_blue)+"\n"
	
	def saveFile(self,text,filename):
		output = open(filename,'a')
		output.write(text)
		output.close()
		return True


if __name__=='__main__':
	issueNo = [
]
	for issue in issueNo:
		spider = Spider(issue)
		page = spider.getPage()
		result = spider.getHit(page)
		text = spider.createSqlOrTxt(result,'sql')
		output = spider.saveFile(text,'/home/april/ssq.sql')
		if output:
			print "success"
		else:
			print issue






