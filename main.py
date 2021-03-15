import requests
import re
import urllib
import os
import time
from PIL import Image

class Downloader():
    def __init__(self):
        pass

    def download(self,htmlPath,outputPath):
        with open(htmlPath,'r',encoding='UTF-8') as f:
            html=f.read()
        urlList=self.getPageURLList(html)
        self.mergeToPDF(urlList,outputPath)

    def mergeToPDF(self,urlList,outputPath):
        timeStamp=str(int(time.time()*1000))
        os.makedirs(timeStamp)
        pathList=[]
        for index,url in enumerate(urlList):
            path=timeStamp+'/'+str(index)+'.jpg'
            urllib.request.urlretrieve(url,path)
            pathList.append(path)

        file=Image.open(pathList[0])
        imageList=[]

        for index in range(1,len(pathList)):
            image=Image.open(pathList[index])
            imageList.append(image)

        file.save(outputPath,'PDF',resolution=100.0,save_all=True,append_images=imageList)

        self.deleteDir(timeStamp)

    def getPageURLList(self,html):
        cpl1 = re.compile('src=".*?" alt="ppt"')
        imgList = re.findall(cpl1, html)
        length = int(len(imgList) / 2)
        urlList = []
        for index in range(length):
            url = imgList[index + length][5:-11]
            urlList.append(url)
        return urlList

    def deleteDir(self,dirPath):
        dirList = os.listdir(dirPath)
        for file in dirList:
            path = dirPath + '/' + file
            os.remove(path)
        os.rmdir(dirPath)

if __name__ == '__main__':
    htmlPath='html.txt'
    outputPath='demo.pdf'
    downloader=Downloader()
    downloader.download(htmlPath,outputPath)