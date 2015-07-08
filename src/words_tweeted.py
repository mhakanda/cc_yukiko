from sys import argv
import collections

script, input1, input2 = argv
tweets = []
words = []
index = {}
maxlen = 0

fIn = open(input1, 'r')

#read input file
for line in fIn:
	tweets.append(line)

fIn.close()

def add_to_index(index, keyword):
	global maxlen
	if keyword in index: #keyword is existing in index
		index[keyword] += 1 #increment word count 
	else: #create index with new keyword
		index[keyword] = 1
		if len(keyword) > maxlen: #get max length among all words
			maxlen = len(keyword) 

for tw in tweets:
	words = tw.split() #break down to each word
	for word in words:
		add_to_index(index, word) 
		
#sorting by alphabetical order
sortedIndex = collections.OrderedDict(sorted(index.items()))

#create output file
fOut = open(input2,'w')
for word, count in sortedIndex.iteritems():
	#calc space for indent
	sp = maxlen - len(word) - len(str(count)) + 7 
	#output
	fOut.write(word + (' ' * sp) + str(count) + '\n')

fOut.close()