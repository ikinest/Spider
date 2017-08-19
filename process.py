__author__ = 'ikinest'
"""
A tool for adding split flag to construct a list.
"""

class Process(object):
	def __init__(self):
		self.split1="'"
		self.split2="',"
	def addSplit(self,content):
		return self.split1+str(content)+self.split2
	def writeFile(self,output,splitedContent):
		f = open(output,'a')
		f.write(splitedContent+"\n")
		
if __name__ == "__main__":
	pro = Process()
	inputfile= '/home/april/1.txt'
	outputfile = '/home/april/2.txt'
	f = open(inputfile)
	for line in f.readlines():
		if line.strip() !='':
			pro.writeFile(outputfile,pro.addSplit(line.strip()))
