# Anne Tran (UCID: 30286177)
# Assign2_Q2

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

# Only keep word has more than and equal to 2 characters
for word in splitFile:
    if len(word)>=2:
        twoCharList.append(word)
    else:
        twoCharList=twoCharList



