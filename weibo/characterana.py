# encoding='utf-8'


import jieba
import string
import sys
import os
import csv
import jieba.posseg as pseg

jieba.enable_paddle()

jieba.load_userdict("C:\\Users\\moban\\Documents\\Cassis\\weibo-search\\weibo\\dict_baidu_utf8.txt")
jieba.load_userdict("C:\\Users\\moban\\Documents\\Cassis\\weibo-search\\weibo\\dict_pangu.txt")
jieba.load_userdict("C:\\Users\\moban\\Documents\\Cassis\\weibo-search\\weibo\\dict_sougou_utf8.txt")
jieba.load_userdict("C:\\Users\\moban\\Documents\\Cassis\\weibo-search\\weibo\\dict_tencent_utf8.txt")
jieba.load_userdict("C:\\Users\\moban\\Documents\\Cassis\\weibo-search\\weibo\\SogouLabDic.txt")

stopwords = {}.fromkeys([ line.rstrip() for line in open('C:\\Users\\moban\\Documents\\Cassis\\weibo-search\\weibo\\Stopword.txt',encoding='utf-8' )])
with open('C:\\Users\\moban\\Documents\\Cassis\\weibo-search\\weibo\\安迪.csv',encoding='utf-8')as csvfile:
        reader=csv.reader(csvfile)
        column=[row[0] for row in reader]

index_weibo = len(column)



def get_data(index_weibo):
   
    
    result=[]

    #seg = jieba.lcut(column[index_weibo],cut_all=False)
    words=pseg.cut(column[index_weibo],paddle=True)

    for i,flag in words:
        if i not in stopwords:
            h=i+flag
            result.append(h)
    
    fo=open('C:\\Users\\moban\\Documents\\Cassis\\weibo-search\\weibo\\character_full.dat','a+',encoding='utf-8')

    for j in result:
        fo.write(j)
        fo.write(' ')
    
    fo.write('\r\n')
    fo.close()
        
    

if __name__=='__main__':

    total_weibo= index_weibo
    print("进程开始...")
    for index_weibo in range(1,total_weibo):
        
        get_data(index_weibo)
       
        
    print("Done!")

