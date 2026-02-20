f = open('MyData','r')

fis = open('abc','w')

for data in f:
    fis.write(data)

imgFile = open('imgCopy.jpg','wb')

imgOrig = open('mohitPhoto.jpg','rb')

for data in imgOrig:
    imgFile.write(data)