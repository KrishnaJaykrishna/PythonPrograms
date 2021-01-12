def swapData():
    file1 = input('Enter The File Name')
    file2 = input('Enter The File Name')
    with open(file1,'r') as a :
        dataa = a.read()
    with open(file2,'r') as b :
        datab = b.read()
    with open (file1,'w') as a :
        a.write(datab)
    with open (file2,'w') as b :
        b.write(dataa)
swapData()
