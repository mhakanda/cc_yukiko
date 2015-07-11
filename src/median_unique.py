from sys import argv
import math
import datetime

script, input1, input2, input3 = argv
newTwCnt = 0
wordCnt = 0
logTwCnt = 0

def calc_median(wordCnt, newTwCnt):
	val = 0
	val = float(wordCnt) / float(newTwCnt) 
	val = '{0:g}'.format(math.floor(val*100)/100) #truncate to 2 decimal places
	return str(val)

def count_new_tweet(twAll,fOut):
	global newTwCnt, wordCnt
	#count words of new tweets
	for line in twAll[logTwCnt:len(twAll)]:
		tw = line.split() #split sentences into words
		tw = {}.fromkeys(tw).keys() #get only unique words

		wordCnt += len(tw) #add the number of words
		newTwCnt += 1 #increment the number of tweets

		#calculate median
		medVal = calc_median(wordCnt,newTwCnt)
		#output result to ft2.txt
		fOut.write(medVal + '\n') 
	return medVal

#open tweets.txt in read mode
fIn = open(input1, 'r')
twAll = fIn.readlines()
fIn.close()

#open log.txt in read/write mode
flog = open(input3,'a+')
log = flog.readlines()
llog = []

#get infomation from log.txt
if len(log) != 0:
	llog = log[len(log) -1].rstrip() #remove enter code('\n')
	llog = llog.split(',') #turn into list seperated with commas
	wordCnt = int(llog[1]) #count number of words from last run 
	logTwCnt = int(llog[2]) #count number of tweets from last run
	logMedVal = str(llog[3]) #read median from last run
	newTwCnt = int(llog[2]) #count number of new tweets
else: #log.txt doesn't exist 
	flog.write('Timestamp,Total Words,Total Tweets,Median\n')
	
#open ft2.txt in write mode
fOut = open(input2,'a')

#calculate median and write file  
if (len(twAll) - logTwCnt) != 0: #when new tweets exist 
	logMedVal = count_new_tweet(twAll, fOut)

fOut.close()

#get timestamp
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#write log.txt file
flog.write( now + ',' + str(wordCnt) + ',' + str(newTwCnt) + ',' + logMedVal + '\n')

flog.close()
