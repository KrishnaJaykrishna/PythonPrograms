string = input('Enter Your String')
print (string)
characterCount = 0
wordCount = 1
for i in string :
        characterCount = characterCount + 1
        if (i==' '):
            wordCount=wordCount+1
            characterCount=characterCount-1
print (characterCount)
print(wordCount)
