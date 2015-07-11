from sys import argv
import collections

script, input1, input2 = argv
tweets = []
words = []
index = {}
maxlen = 0

#open tweets.txt in read mode
fIn = open(input1, 'r')

#read input file
for line in fIn:
	tweets.append(line)
	
fIn.close()

def add_to_index(index, keyword):
	global maxlen
	if keyword in index: #keyword exists in index
		index[keyword] += 1 #increment word count 
	else: #create index with a new keyword
		index[keyword] = 1
		if len(keyword) > maxlen: #get max length for all words
			maxlen = len(keyword) 

for tw in tweets:
	words = tw.split() #turn into list seperated with spaces
	for word in words:
		add_to_index(index, word) 
		
#sort by alphabetical order
sortedIndex = collections.OrderedDict(sorted(index.items()))

#create output file
fOut = open(input2,'w')
for word, count in sortedIndex.iteritems():
	#calculate space for indent
	sp = maxlen - len(word) - len(str(count)) + 7 
	#output
	fOut.write(word + (' ' * sp) + str(count) + '\n')

fOut.close()