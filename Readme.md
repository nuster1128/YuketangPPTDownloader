# 雨课堂课件下载器

## 版本信息

### Version 1.0

2021.3.15完成1.0版本

## 项目目的

老师在雨课堂讲课时会播放PPT，雨课堂虽然支持打印导出PPT为PDF，但是大课件好像是很难导出的，会卡在那里生死不定(bushi)。

比如今天(2021.3.15)我打算导出多媒体信息处理的416张PPT课件时，就卡在那里不动了。

作为一个野生程序员(x)自然不能认输，所以反手花一个小时写了这个爬取课件的程序。

主要是根据网页源码找到每一张课件的url，然后下载下来对应图片，之后再合成一个PDF输出。

没啥难的，就是spider+PDF和OS处理。

## 主要功能

获取雨课堂中老师讲课过程中播放的高清课件图片，并整合为一个PDF。

## 使用方式

1.将“打印课件页面”的源码以文本方式下载到项目目录下。

2.修改main.py中的源码文本输入路径和PDF输出路径。

3.运行main.py。然后就可以在输出路径看到PDF了。

样例详见项目目录，其中 html.txt 里就是源码文本，demo.pdf就是运行main.py生成的PDF课件。

## 项目依赖库

Python 3.7

requests,re,urllib,os,time,PIL

## 作者联系方式

Email:wfzhangzeyu@163.com

QQ:997577114