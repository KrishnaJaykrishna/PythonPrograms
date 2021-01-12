def countingWordsfromfile():
    f = input('Enter The File Name')
    file = open(f,'r')
    numberOfWords = 0
    for line in file:
        words = line.split()
        numberOfWords = numberOfWords + len(words)
    print  (numberOfWords)

countingWordsfromfile()
