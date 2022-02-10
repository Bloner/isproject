from datetime import datetime
import re
import csv
import os
import requests


def processdata():
    csv_path = "C:/Users/Bonn/Desktop/1.csv"
    with open(csv_path) as f:
        reader = csv.reader(f)
        n = 1
        for each_row in reader:
            each_row[1] = findurl(each_row[1])
            print("Downloading the " + str(n) + "th video, the link is " + each_row[1] + "...")
            download(each_row[1], each_row[0][-19:])
            print("The " + str(n) + "th video has been downloaded successfully!")
            n += 1
    f.close()


def download(url, name):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    path = "C:/Users/Bonn/Desktop/videos/" + name + ".mp4"
    time.sleep(random.randomint(20, 30))
    print("what happends?")
    r = requests.get("https" + url, headers=header)
    with open(path, 'wb') as f:
        f.write(r.content)
        f.close


# convert string to number, like "2.3w" -> 23000 and "2.3亿" to 230000000
def strToNum(s):
    if s[-1] == "w":
        res= int(float(s[0:-1]) * 10000)
    elif s[-1] == "亿":
        res = int(float(s[0:-1]) * 100000000)
    else:
        res = s
    return res


# convert string to date, like "发布时间：2021-10-23 17:25" -> 2021-10-23 17:25
def strToDate(s):
    s = s[5:]
    ls = re.split('-| |:',s)
    ls = [int(x) for x in ls]
    return datetime(ls[0], ls[1], ls[2], ls[3], ls[4])


# get the video url from the html context
def findurl(src):
    rule = r'src=""(.*?)""'
    res = re.findall(rule, src)
    return res[-1]


# rename file based on the order and settled name in a file
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
   processdata()
'''
path = 'C:\\Users\\Bonn\\Desktop\\videoInfoBasedOnKW'
#set working directory
os.chdir(path)

pd.read_csv(f) // read from path f

combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig') // write pd back to file

'''