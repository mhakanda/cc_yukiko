# example of program that calculates the median number of unique words per tweet.
from sys import argv
import time

script, input1, input2 = argv
lineCnt = 0
wordCnt = 0

def count_old_tweet(twAll):
	global lineCnt, wordCnt
	#count words from first tweet to the last calculated tweet
	for line in twAll[0:oldTwCnt]:
		tw = line.split()
		wordCnt += len(tw) #number of words
	lineCnt = oldTwCnt #number of tweets

def count_new_tweet(twAll,fOut):
	global lineCnt, wordCnt
	#count words of new tweets
	for line in twAll[oldTwCnt:len(twAll)]:
		tw = line.split()
		wordCnt += len(tw)
		lineCnt += 1
		medianval = round(float(wordCnt) / float(lineCnt),1) #calc median
		#print len(tw), wordCnt, lineCnt, medianval
		fOut.write(str(medianval) + '\n')

#t0 = time.clock()

#read tweets.txt
fIn = open(input1, 'r')
twAll = fIn.readlines()
fIn.close()

#read/write ft2.txt
fOut = open(input2,'a+')
oldOut = fOut.readlines()
oldTwCnt = len(oldOut) #number of tweets in the last run

#get total number of words until last run
if oldTwCnt != 0: #existing results in ft2.txt
	count_old_tweet(twAll) 

#get mean number of word and write file  
if (len(twAll) - oldTwCnt) != 0: #existing new tweet
	count_new_tweet(twAll, fOut)

fOut.close()

#t1 = time.clock()

#print("dt0="+str(t1-t0)+"[s]")
