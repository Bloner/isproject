from datetime import datetime
import re
import pandas as pd
import os

#convert string to number, like "2.3w" -> 23000 and "2.3亿" to 230000000
def strToNum(s):
    if s[-1] == "w":
        res= int(float(s[0:-1]) * 10000)
    elif s[-1] == "亿":
        res = int(float(s[0:-1]) * 100000000)
    else:
        res = s
    return res

#convert string to date, like "发布时间：2021-10-23 17:25" -> 2021-10-23 17:25
def strToDate(s):
    s = s[5:]
    ls = re.split('-| |:',s)
    ls = [int(x) for x in ls]
    return datetime(ls[0], ls[1], ls[2], ls[3], ls[4])


#get the video url from the html context
def findVideoSrc(src):
    for eachString in src:
        pass

#rename file based on the order and settled name in a file
def renameFile():
    path = ""
    fileList = os.listdir(path).sort()

    n = 0
    for i in fileList:
        oldName = path + os.sep + fileList[n]
        newName = path + os.sep + 'a' + str(n+1) + '.JPG'

        os.rename(oldName, newName)
        print(oldName, "----->", newName)
        n+=1
if __name__ == "__main__":
    print(strToDate("发布时间：2022-10-12 23:56"))

'''
path = r'C:\Users\Bonn\Desktop\videoInfoBasedOnKW'
#set working directory
os.chdir(path)

pd.read_csv(f) // read from path f

combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig') // write pd back to file

'''