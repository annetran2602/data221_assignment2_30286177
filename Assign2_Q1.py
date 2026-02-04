# Anne Tran (UCID: 30286177)
# Assign2_Q1

# Open the file
inputFile=open('sample-file.txt', mode='r')
file=inputFile.read()

lowercaseFile=file.lower() # change to lowercase

#Remove punctuation
noPuncFile=lowercaseFile.replace(",", " ") # Remove ","
noPuncFile=noPuncFile.replace(".", " ") # Remove "."

# Split into words
splitFile=noPuncFile.split()
twoCharList=[]


for word in splitFile:
    if len(word)>=2:
        twoCharList.append(word)
    else:
        twoCharList=twoCharList


wordDict={}
for word in twoCharList:
    if word not in wordDict.keys():
        wordDict[word]=1
    else:
        wordDict[word]+=1


sortedWordDict=dict(sorted(wordDict.items(), key=lambda item: item[1], reverse=True))

# Print out the 10 most frequent word from the dict
count=1
for word, wordCount in sortedWordDict.items():
    if count >10:
        break # stop printing
    print(word, "->", wordCount,end=" ") #print word & its wordCount in one line
    count+=1




